"""
Pydantic request / response schemas for the iPaL API.
"""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


# ──────────────────────────────────────────────────
# Source Citations
# ──────────────────────────────────────────────────
class SourceCitation(BaseModel):
    document: str = Field(..., description="Source document filename")
    chunk_text: str = Field("", description="Relevant text snippet")
    score: float = Field(0.0, description="Relevance score")
    page: int | None = Field(None, description="Page number if available")
    category: str | None = Field(None, description="Document category")


# ──────────────────────────────────────────────────
# Chat Messages
# ──────────────────────────────────────────────────
class ChatMessageRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000, description="User message text")
    session_id: UUID | None = Field(None, description="Existing session ID, or null to create a new one")


class ChatMessageResponse(BaseModel):
    session_id: UUID
    message_id: UUID
    response: str
    sources: list[SourceCitation] = []
    confidence_score: float | None = None
    latency_ms: int | None = None
    created_at: datetime

    model_config = {"from_attributes": True}


# ──────────────────────────────────────────────────
# Chat Sessions
# ──────────────────────────────────────────────────
class ChatSessionCreate(BaseModel):
    title: str = Field("New Chat", max_length=255)


class ChatSessionResponse(BaseModel):
    id: UUID
    title: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    message_count: int = 0

    model_config = {"from_attributes": True}


class MessageItem(BaseModel):
    id: UUID
    role: str
    content: str
    sources: list[SourceCitation] = []
    confidence_score: float | None = None
    created_at: datetime

    model_config = {"from_attributes": True}


class ChatHistoryResponse(BaseModel):
    session_id: UUID
    title: str
    messages: list[MessageItem] = []


# ──────────────────────────────────────────────────
# Health & Status
# ──────────────────────────────────────────────────
class HealthResponse(BaseModel):
    status: str
    version: str
    uptime_seconds: float


class ComponentStatus(BaseModel):
    status: str
    details: dict = {}


class StatusResponse(BaseModel):
    status: str
    database: ComponentStatus
    vector_db: ComponentStatus
    llm: ComponentStatus
    redis: ComponentStatus


# ──────────────────────────────────────────────────
# Document Ingestion
# ──────────────────────────────────────────────────
class IngestRequest(BaseModel):
    category: str | None = Field(None, description="Document category tag")
    force_reprocess: bool = Field(False, description="Re-process already ingested documents")


class IngestStatusResponse(BaseModel):
    job_id: UUID
    status: str
    total_documents: int
    processed_documents: int
    failed_documents: int
    started_at: datetime | None = None
    completed_at: datetime | None = None

    model_config = {"from_attributes": True}


# ──────────────────────────────────────────────────
# Auth
# ──────────────────────────────────────────────────
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=100)
    email: str = Field(..., max_length=255)
    password: str = Field(..., min_length=8)


class UserResponse(BaseModel):
    id: UUID
    username: str
    email: str
    role: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
