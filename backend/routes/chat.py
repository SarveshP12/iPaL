"""
Chat API routes — message sending, session management, and chat history.
"""

import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from db.database import get_db
from models.models import ChatSession, ChatMessage
from schemas.schemas import (
    ChatMessageRequest,
    ChatMessageResponse,
    ChatSessionCreate,
    ChatSessionResponse,
    ChatHistoryResponse,
    MessageItem,
)
from services.rag_service import rag_service

router = APIRouter(prefix="/api/chat", tags=["Chat"])


# ── POST /api/chat/message ───────────────────────
@router.post("/message", response_model=ChatMessageResponse)
async def send_message(
    request: ChatMessageRequest,
    db: AsyncSession = Depends(get_db),
):
    """Send a message to the chatbot and get a RAG-powered response."""

    # Get or create session
    session_id = request.session_id
    if session_id:
        result = await db.execute(select(ChatSession).where(ChatSession.id == session_id))
        session = result.scalar_one_or_none()
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")
    else:
        session = ChatSession(
            id=uuid.uuid4(),
            title=request.message[:50] + ("..." if len(request.message) > 50 else ""),
        )
        db.add(session)
        await db.flush()
        session_id = session.id

    # Save user message
    user_msg = ChatMessage(
        id=uuid.uuid4(),
        session_id=session_id,
        role="user",
        content=request.message,
    )
    db.add(user_msg)

    # Build conversation history from session
    history_result = await db.execute(
        select(ChatMessage)
        .where(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at.desc())
        .limit(10)
    )
    history_msgs = history_result.scalars().all()
    conversation_history = [
        {"role": m.role, "content": m.content}
        for m in reversed(history_msgs)
    ]

    # RAG query
    rag_result = await rag_service.query(
        question=request.message,
        conversation_history=conversation_history,
    )

    # Save assistant response
    assistant_msg = ChatMessage(
        id=uuid.uuid4(),
        session_id=session_id,
        role="assistant",
        content=rag_result["response"],
        sources=[s.model_dump() for s in rag_result["sources"]],
        confidence_score=rag_result.get("confidence_score"),
        token_count=rag_result.get("token_count"),
        latency_ms=rag_result.get("latency_ms"),
    )
    db.add(assistant_msg)
    await db.flush()

    return ChatMessageResponse(
        session_id=session_id,
        message_id=assistant_msg.id,
        response=rag_result["response"],
        sources=rag_result["sources"],
        confidence_score=rag_result.get("confidence_score"),
        latency_ms=rag_result.get("latency_ms"),
        created_at=datetime.now(timezone.utc),
    )


# ── POST /api/chat/session ───────────────────────
@router.post("/session", response_model=ChatSessionResponse)
async def create_session(
    request: ChatSessionCreate,
    db: AsyncSession = Depends(get_db),
):
    """Create a new chat session."""
    session = ChatSession(id=uuid.uuid4(), title=request.title)
    db.add(session)
    await db.flush()
    return ChatSessionResponse(
        id=session.id,
        title=session.title,
        is_active=True,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
        message_count=0,
    )


# ── GET /api/chat/sessions ──────────────────────
@router.get("/sessions", response_model=list[ChatSessionResponse])
async def list_sessions(db: AsyncSession = Depends(get_db)):
    """List all chat sessions."""
    result = await db.execute(
        select(
            ChatSession,
            func.count(ChatMessage.id).label("msg_count"),
        )
        .outerjoin(ChatMessage, ChatMessage.session_id == ChatSession.id)
        .group_by(ChatSession.id)
        .order_by(ChatSession.updated_at.desc())
        .limit(50)
    )
    rows = result.all()
    return [
        ChatSessionResponse(
            id=session.id,
            title=session.title,
            is_active=session.is_active,
            created_at=session.created_at,
            updated_at=session.updated_at,
            message_count=msg_count,
        )
        for session, msg_count in rows
    ]


# ── GET /api/chat/history/{session_id} ───────────
@router.get("/history/{session_id}", response_model=ChatHistoryResponse)
async def get_history(session_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    """Get full chat history for a session."""
    result = await db.execute(select(ChatSession).where(ChatSession.id == session_id))
    session = result.scalar_one_or_none()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    msgs_result = await db.execute(
        select(ChatMessage)
        .where(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at.asc())
    )
    messages = msgs_result.scalars().all()

    return ChatHistoryResponse(
        session_id=session.id,
        title=session.title,
        messages=[
            MessageItem(
                id=m.id,
                role=m.role,
                content=m.content,
                sources=m.sources or [],
                confidence_score=m.confidence_score,
                created_at=m.created_at,
            )
            for m in messages
        ],
    )


# ── DELETE /api/chat/session/{session_id} ────────
@router.delete("/session/{session_id}")
async def delete_session(session_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    """Delete a chat session and all its messages."""
    result = await db.execute(select(ChatSession).where(ChatSession.id == session_id))
    session = result.scalar_one_or_none()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    await db.delete(session)
    return {"detail": "Session deleted", "session_id": str(session_id)}
