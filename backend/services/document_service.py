"""
Document Service — handles document loading, preprocessing, chunking, and ingestion.

Pipeline: Load → Extract Text → Clean → Chunk → Embed → Store in Qdrant
"""

import hashlib
import logging
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client.http.models import PointStruct

from config.settings import settings
from db.qdrant_setup import get_qdrant_client
from services.embedding_service import embedding_service

logger = logging.getLogger(__name__)


# ──────────────────────────────────────────────────
# Text extractors
# ──────────────────────────────────────────────────
def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""
    from pypdf import PdfReader

    reader = PdfReader(file_path)
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)
    return "\n\n".join(pages)


def extract_text_from_docx(file_path: str) -> str:
    """Extract text from a DOCX file."""
    from docx import Document as DocxDocument

    doc = DocxDocument(file_path)
    return "\n\n".join(para.text for para in doc.paragraphs if para.text.strip())


def extract_text_from_txt(file_path: str) -> str:
    """Extract text from a plain text file."""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def extract_text_from_html(file_path: str) -> str:
    """Extract text from an HTML file."""
    from bs4 import BeautifulSoup

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    return soup.get_text(separator="\n", strip=True)


EXTRACTORS = {
    ".pdf": extract_text_from_pdf,
    ".docx": extract_text_from_docx,
    ".txt": extract_text_from_txt,
    ".html": extract_text_from_html,
    ".htm": extract_text_from_html,
    ".md": extract_text_from_txt,
}


# ──────────────────────────────────────────────────
# Text cleaning
# ──────────────────────────────────────────────────
def clean_text(text: str) -> str:
    """Normalise whitespace, remove excessive blank lines."""
    import re

    text = re.sub(r"\r\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


# ──────────────────────────────────────────────────
# Chunking
# ──────────────────────────────────────────────────
def chunk_text(text: str) -> list[str]:
    """Split text into overlapping chunks using recursive character splitter."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    return splitter.split_text(text)


# ──────────────────────────────────────────────────
# File utilities
# ──────────────────────────────────────────────────
def compute_checksum(file_path: str) -> str:
    """SHA-256 checksum for change detection / dedup."""
    sha = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(8192), b""):
            sha.update(block)
    return sha.hexdigest()


def detect_doc_type(file_path: str) -> str:
    """Return normalised file extension."""
    return Path(file_path).suffix.lower().lstrip(".")


# ──────────────────────────────────────────────────
# Document Service
# ──────────────────────────────────────────────────
class DocumentService:
    """End-to-end document ingestion pipeline."""

    def __init__(self):
        self._qdrant = get_qdrant_client()
        self._collection = settings.QDRANT_COLLECTION_NAME

    # ── Single document pipeline ─────────────────

    def ingest_file(
        self,
        file_path: str,
        category: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict:
        """
        Process a single file: extract → clean → chunk → embed → upsert to Qdrant.

        Returns a summary dict with chunk count and status.
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Document not found: {file_path}")

        ext = path.suffix.lower()
        if ext not in EXTRACTORS:
            raise ValueError(f"Unsupported file type: {ext}")

        logger.info("Ingesting document: %s", path.name)

        # 1. Extract text
        raw_text = EXTRACTORS[ext](file_path)
        if not raw_text.strip():
            logger.warning("Empty text extracted from %s", path.name)
            return {"filename": path.name, "status": "skipped", "chunk_count": 0}

        # 2. Clean
        cleaned = clean_text(raw_text)

        # 3. Chunk
        chunks = chunk_text(cleaned)
        logger.info("Created %d chunks from %s", len(chunks), path.name)

        # 4. Embed
        vectors = embedding_service.embed_batch(chunks)

        # 5. Prepare metadata
        checksum = compute_checksum(file_path)
        base_meta = {
            "source": path.name,
            "doc_type": detect_doc_type(file_path),
            "category": category or "general",
            "file_path": str(path.absolute()),
            "checksum": checksum,
            "created_at": datetime.utcnow().isoformat(),
        }
        if metadata:
            base_meta.update(metadata)

        # Remove existing chunks for this source to prevent duplication
        from qdrant_client.http.models import Filter, FieldCondition, MatchValue
        self._qdrant.delete(
            collection_name=self._collection,
            points_selector=Filter(
                must=[
                    FieldCondition(
                        key="source",
                        match=MatchValue(value=path.name)
                    )
                ]
            )
        )
        logger.info("Cleared existing chunks for source: %s", path.name)

        # 6. Upsert to Qdrant
        points = []
        for i, (chunk, vector) in enumerate(zip(chunks, vectors)):
            point_id = str(uuid.uuid4())
            payload = {
                **base_meta,
                "chunk_index": i,
                "chunk_text": chunk,
                "total_chunks": len(chunks),
            }
            points.append(PointStruct(id=point_id, vector=vector, payload=payload))

        # Batch upsert (100 at a time)
        batch_size = 100
        for start in range(0, len(points), batch_size):
            batch = points[start : start + batch_size]
            self._qdrant.upsert(
                collection_name=self._collection,
                points=batch,
            )

        logger.info("Upserted %d points for %s", len(points), path.name)

        return {
            "filename": path.name,
            "status": "completed",
            "chunk_count": len(chunks),
            "checksum": checksum,
        }

    # ── Batch ingestion ──────────────────────────

    def ingest_directory(
        self,
        directory: str | None = None,
        category: str | None = None,
        force: bool = False,
    ) -> dict:
        """
        Ingest all supported documents from a directory.

        Returns summary with counts.
        """
        dir_path = Path(directory or settings.DOCUMENT_STORAGE_PATH)
        if not dir_path.exists():
            logger.warning("Document directory does not exist: %s", dir_path)
            return {"status": "error", "message": f"Directory not found: {dir_path}"}

        results = {
            "total": 0,
            "processed": 0,
            "failed": 0,
            "skipped": 0,
            "details": [],
        }

        supported_files = [
            f
            for f in dir_path.rglob("*")
            if f.is_file() and f.suffix.lower() in EXTRACTORS
        ]
        results["total"] = len(supported_files)

        for file_path in supported_files:
            try:
                result = self.ingest_file(
                    str(file_path),
                    category=category,
                )
                if result["status"] == "completed":
                    results["processed"] += 1
                else:
                    results["skipped"] += 1
                results["details"].append(result)
            except Exception as exc:
                results["failed"] += 1
                results["details"].append(
                    {"filename": file_path.name, "status": "failed", "error": str(exc)}
                )
                logger.error("Failed to ingest %s: %s", file_path.name, exc)

        return results

    # ── Delete operations ────────────────────────

    def delete_by_source(self, source_filename: str) -> int:
        """Delete all vectors associated with a specific source document."""
        from qdrant_client.http.models import Filter, FieldCondition, MatchValue

        self._qdrant.delete(
            collection_name=self._collection,
            points_selector=Filter(
                must=[
                    FieldCondition(field_name="source", match=MatchValue(value=source_filename))
                ]
            ),
        )
        logger.info("Deleted all points for source: %s", source_filename)
        return 0  # Qdrant delete doesn't return count directly

    def get_collection_stats(self) -> dict:
        """Return collection statistics."""
        info = self._qdrant.get_collection(self._collection)
        return {
            "collection": self._collection,
            "vectors_count": info.vectors_count,
            "points_count": info.points_count,
            "status": str(info.status),
        }


# Module-level singleton
document_service = DocumentService()
