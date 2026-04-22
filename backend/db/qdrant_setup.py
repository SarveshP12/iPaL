"""
Qdrant vector database client and collection initialisation.
"""

import logging

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PayloadSchemaType

from config.settings import settings

logger = logging.getLogger(__name__)

_qdrant_client: QdrantClient | None = None


def get_qdrant_client() -> QdrantClient:
    """Singleton Qdrant client."""
    global _qdrant_client
    if _qdrant_client is None:
        _qdrant_client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT,
            api_key=settings.QDRANT_API_KEY or None,
            timeout=30,
        )
    return _qdrant_client


def init_qdrant() -> None:
    """
    Create the Qdrant collection if it does not already exist.
    Configures HNSW index with cosine similarity and payload indexes
    for metadata filtering.
    """
    client = get_qdrant_client()
    collection_name = settings.QDRANT_COLLECTION_NAME

    collections = client.get_collections().collections
    exists = any(col.name == collection_name for col in collections)

    if not exists:
        logger.info(
            "Creating Qdrant collection '%s' (dim=%d, metric=cosine)",
            collection_name,
            settings.EMBEDDING_DIMENSION,
        )
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=settings.EMBEDDING_DIMENSION,
                distance=Distance.COSINE,
            ),
        )

        # Create payload indexes for efficient metadata filtering
        for field, schema in [
            ("source", PayloadSchemaType.KEYWORD),
            ("doc_type", PayloadSchemaType.KEYWORD),
            ("category", PayloadSchemaType.KEYWORD),
            ("created_at", PayloadSchemaType.DATETIME),
        ]:
            client.create_payload_index(
                collection_name=collection_name,
                field_name=field,
                field_schema=schema,
            )

        logger.info("Collection '%s' created with payload indexes.", collection_name)
    else:
        logger.info("Collection '%s' already exists — skipping.", collection_name)


def health_check() -> dict:
    """Return Qdrant health information."""
    try:
        client = get_qdrant_client()
        info = client.get_collection(settings.QDRANT_COLLECTION_NAME)
        return {
            "status": "healthy",
            "vectors_count": info.vectors_count,
            "points_count": info.points_count,
            "collection": settings.QDRANT_COLLECTION_NAME,
        }
    except Exception as exc:
        return {"status": "unhealthy", "error": str(exc)}