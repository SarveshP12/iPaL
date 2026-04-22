"""
RAG Service — Retrieval-Augmented Generation pipeline.

Flow: Embed query → Qdrant search → Build context → LLM generate → Return with citations
"""

import logging
from typing import Any

from qdrant_client.http.models import Filter, FieldCondition, MatchValue

from config.settings import settings
from db.qdrant_setup import get_qdrant_client
from services.embedding_service import embedding_service
from services.llm_service import llm_service
from schemas.schemas import SourceCitation

logger = logging.getLogger(__name__)


class RAGService:
    def __init__(self):
        self._qdrant = get_qdrant_client()
        self._collection = settings.QDRANT_COLLECTION_NAME

    def retrieve(self, query: str, top_k: int = 5, score_threshold: float = 0.3, category_filter: str | None = None) -> list[dict]:
        query_vector = embedding_service.embed(query)
        search_filter = None
        if category_filter:
            search_filter = Filter(must=[FieldCondition(field_name="category", match=MatchValue(value=category_filter))])

        results = self._qdrant.search(
            collection_name=self._collection, query_vector=query_vector,
            limit=top_k, score_threshold=score_threshold,
            query_filter=search_filter, with_payload=True,
        )
        return [{"chunk_text": h.payload.get("chunk_text",""), "source": h.payload.get("source","Unknown"), "category": h.payload.get("category",""), "chunk_index": h.payload.get("chunk_index",0), "score": round(h.score,4), "doc_type": h.payload.get("doc_type","")} for h in results]

    @staticmethod
    def build_context(chunks: list[dict]) -> str:
        if not chunks:
            return "No relevant documents found."
        return "\n\n".join(f"[Source {i}: {c['source']} (relevance: {c['score']:.2f})]\n{c['chunk_text']}" for i, c in enumerate(chunks, 1))

    @staticmethod
    def build_citations(chunks: list[dict]) -> list[SourceCitation]:
        citations, seen = [], set()
        for c in chunks:
            if c["source"] not in seen:
                seen.add(c["source"])
                citations.append(SourceCitation(document=c["source"], chunk_text=c["chunk_text"][:200], score=c["score"], category=c.get("category")))
        return citations

    async def query(self, question: str, conversation_history: list[dict] | None = None, top_k: int = 5, category_filter: str | None = None) -> dict[str, Any]:
        retrieved = self.retrieve(query=question, top_k=top_k, category_filter=category_filter)
        context = self.build_context(retrieved)
        llm_result = await llm_service.generate(question=question, context=context, conversation_history=conversation_history)
        citations = self.build_citations(retrieved)
        return {"response": llm_result["response"], "sources": citations, "confidence_score": llm_result.get("confidence_score"), "token_count": llm_result.get("token_count"), "latency_ms": llm_result.get("latency_ms")}

    def health_check(self) -> dict:
        return {"embedding": embedding_service.health_check(), "vector_db": True, "llm": llm_service.health_check()}

rag_service = RAGService()
