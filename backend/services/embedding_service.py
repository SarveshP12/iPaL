"""
Embedding Service — wraps sentence-transformers for vector generation.

Provides:
- Single-text embedding
- Batch embedding
- Cached embedding (in-memory LRU)
"""

import logging
from functools import lru_cache

from sentence_transformers import SentenceTransformer

from config.settings import settings

logger = logging.getLogger(__name__)


class EmbeddingService:
    """Generates embeddings using a sentence-transformers model."""

    _instance: "EmbeddingService | None" = None
    _model: SentenceTransformer | None = None

    def __new__(cls) -> "EmbeddingService":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def _get_model(self) -> SentenceTransformer:
        if self._model is None:
            logger.info("Loading embedding model: %s", settings.EMBEDDING_MODEL_NAME)
            self._model = SentenceTransformer(settings.EMBEDDING_MODEL_NAME)
            logger.info(
                "Model loaded — dimension: %d",
                self._model.get_sentence_embedding_dimension(),
            )
        return self._model

    # ── Public API ───────────────────────────────

    @lru_cache(maxsize=1000)
    def embed(self, text: str) -> list[float]:
        """Embed a single text string and return the vector."""
        model = self._get_model()
        vector = model.encode(text, normalize_embeddings=True)
        return vector.tolist()

    def embed_batch(self, texts: list[str], batch_size: int = 64) -> list[list[float]]:
        """Embed a batch of texts. Returns a list of vectors."""
        model = self._get_model()
        vectors = model.encode(
            texts,
            batch_size=batch_size,
            normalize_embeddings=True,
            show_progress_bar=len(texts) > 100,
        )
        return vectors.tolist()

    @property
    def dimension(self) -> int:
        return self._get_model().get_sentence_embedding_dimension()

    def health_check(self) -> dict:
        """Return embedding service health information."""
        try:
            model = self._get_model()
            return {
                "status": "healthy",
                "model": settings.EMBEDDING_MODEL_NAME,
                "dimension": model.get_sentence_embedding_dimension(),
            }
        except Exception as exc:
            return {"status": "unhealthy", "error": str(exc)}


# Module-level convenience singleton
embedding_service = EmbeddingService()
