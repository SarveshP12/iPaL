"""
Admin API routes — document ingestion triggers and system logs.
"""

import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db.database import get_db
from models.models import Document, IngestionJob
from schemas.schemas import IngestStatusResponse
from services.document_service import document_service
from config.settings import settings

import os
import shutil

router = APIRouter(prefix="/api/admin", tags=["Admin"])


@router.post("/ingest", response_model=IngestStatusResponse)
async def trigger_ingestion(
    category: str | None = Form(None),
    force_reprocess: bool = Form(False),
    db: AsyncSession = Depends(get_db),
):
    """Trigger document ingestion from the configured document directory."""
    job = IngestionJob(
        id=uuid.uuid4(),
        status="running",
        started_at=datetime.now(timezone.utc),
    )
    db.add(job)
    await db.flush()

    try:
        result = document_service.ingest_directory(
            category=category,
            force=force_reprocess,
        )
        job.status = "completed"
        job.total_documents = result.get("total", 0)
        job.processed_documents = result.get("processed", 0)
        job.failed_documents = result.get("failed", 0)
        job.completed_at = datetime.now(timezone.utc)

        # Save document records
        for detail in result.get("details", []):
            if detail.get("status") == "completed":
                doc = Document(
                    id=uuid.uuid4(),
                    filename=detail["filename"],
                    file_path=settings.DOCUMENT_STORAGE_PATH,
                    doc_type=detail["filename"].rsplit(".", 1)[-1] if "." in detail["filename"] else "unknown",
                    category=category or "general",
                    chunk_count=detail.get("chunk_count", 0),
                    status="completed",
                    checksum=detail.get("checksum"),
                )
                db.add(doc)
    except Exception as exc:
        job.status = "failed"
        job.error_log = str(exc)
        job.completed_at = datetime.now(timezone.utc)

    await db.flush()
    return IngestStatusResponse(
        job_id=job.id,
        status=job.status,
        total_documents=job.total_documents,
        processed_documents=job.processed_documents,
        failed_documents=job.failed_documents,
        started_at=job.started_at,
        completed_at=job.completed_at,
    )


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    category: str | None = Form(None),
    db: AsyncSession = Depends(get_db),
):
    """Upload a single document and ingest it into the vector store."""
    allowed_extensions = {".pdf", ".docx", ".txt", ".html", ".htm", ".md"}
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {ext}")

    # Save file to disk
    upload_dir = os.path.join(settings.DOCUMENT_STORAGE_PATH, "uploads")
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Ingest
    try:
        result = document_service.ingest_file(file_path, category=category)
        doc = Document(
            id=uuid.uuid4(),
            filename=file.filename,
            file_path=file_path,
            doc_type=ext.lstrip("."),
            category=category or "general",
            chunk_count=result.get("chunk_count", 0),
            status=result.get("status", "completed"),
            checksum=result.get("checksum"),
            file_size_bytes=os.path.getsize(file_path),
        )
        db.add(doc)
        return {"detail": "Document uploaded and ingested", "result": result}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {exc}")


@router.get("/ingest-status/{job_id}", response_model=IngestStatusResponse)
async def get_ingest_status(
    job_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
):
    """Check the status of an ingestion job."""
    result = await db.execute(select(IngestionJob).where(IngestionJob.id == job_id))
    job = result.scalar_one_or_none()
    if not job:
        raise HTTPException(status_code=404, detail="Ingestion job not found")
    return IngestStatusResponse(
        job_id=job.id,
        status=job.status,
        total_documents=job.total_documents,
        processed_documents=job.processed_documents,
        failed_documents=job.failed_documents,
        started_at=job.started_at,
        completed_at=job.completed_at,
    )


@router.get("/documents")
async def list_documents(db: AsyncSession = Depends(get_db)):
    """List all ingested documents."""
    result = await db.execute(
        select(Document).order_by(Document.created_at.desc()).limit(100)
    )
    docs = result.scalars().all()
    return [
        {
            "id": str(d.id),
            "filename": d.filename,
            "doc_type": d.doc_type,
            "category": d.category,
            "chunk_count": d.chunk_count,
            "status": d.status,
            "created_at": d.created_at.isoformat() if d.created_at else None,
        }
        for d in docs
    ]


@router.get("/stats")
async def collection_stats():
    """Get vector database collection statistics."""
    return document_service.get_collection_stats()

@router.post("/cleanup-sessions")
async def cleanup_sessions(db: AsyncSession = Depends(get_db)):
    """Delete expired chat sessions from the database."""
    from sqlalchemy import delete
    from models.models import ChatSession
    
    result = await db.execute(
        delete(ChatSession).where(
            ChatSession.expires_at != None,
            ChatSession.expires_at < datetime.now(timezone.utc)
        )
    )
    return {"detail": "Expired sessions cleaned up", "deleted_count": result.rowcount}

@router.get("/logs")
async def get_system_logs(lines: int = 100):
    """Get recent system logs."""
    log_file = "logs/ipal.log"
    import os
    if not os.path.exists(log_file):
        return {"detail": "Log file not found", "logs": []}
    
    try:
        with open(log_file, "r") as f:
            all_lines = f.readlines()
            return {"logs": all_lines[-lines:]}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
