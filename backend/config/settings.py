"""
iPaL Backend — Centralised Configuration
Uses pydantic-settings to load values from .env with sensible defaults.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ── Application ──
    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    APP_SECRET_KEY: str = "change-me-in-production"
    APP_NAME: str = "iPaL-Backend"
    APP_VERSION: str = "0.1.0"

    # ── Vector Database (Qdrant) ──
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION_NAME: str = "icici_docs"
    QDRANT_API_KEY: str = ""

    # ── Embedding Model ──
    EMBEDDING_MODEL_NAME: str = "sentence-transformers/all-MiniLM-L6-v2"
    EMBEDDING_DIMENSION: int = 384

    # ── LLM Provider ──
    LLM_PROVIDER: str = "google"  # "openai" | "google"
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4o-mini"
    GOOGLE_API_KEY: str = ""
    GOOGLE_MODEL: str = "gemini-2.0-flash"

    # ── PostgreSQL Database ──
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/ipal_db"
    DATABASE_SYNC_URL: str = "postgresql://postgres:postgres@localhost:5432/ipal_db"

    # ── Redis Cache ──
    REDIS_URL: str = "redis://localhost:6379/0"

    # ── JWT Authentication ──
    JWT_SECRET_KEY: str = "change-me-jwt-secret-key"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # ── Document Ingestion ──
    DOCUMENT_STORAGE_PATH: str = "./data/documents"
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 50

    # ── Rate Limiting ──
    RATE_LIMIT_PER_MINUTE: int = 30

    # ── Logging ──
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()