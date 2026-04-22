"""
Health & Status API routes.
"""

import time

from fastapi import APIRouter

from config.settings import settings
from db.qdrant_setup import health_check as qdrant_health
from services.embedding_service import embedding_service
from services.llm_service import llm_service
from schemas.schemas import HealthResponse, StatusResponse, ComponentStatus

router = APIRouter(prefix="/api", tags=["Health"])

_start_time = time.time()


@router.get("/health", response_model=HealthResponse)
async def health():
    """Basic health check — returns OK if the server is running."""
    return HealthResponse(
        status="healthy",
        version=settings.APP_VERSION,
        uptime_seconds=round(time.time() - _start_time, 2),
    )


@router.get("/status", response_model=StatusResponse)
async def detailed_status():
    """Detailed status of all dependent services."""
    # Vector DB
    vdb = qdrant_health()
    vdb_status = ComponentStatus(status=vdb.get("status", "unknown"), details=vdb)

    # LLM
    llm = llm_service.health_check()
    llm_status = ComponentStatus(status=llm.get("status", "unknown"), details=llm)

    # Database — simple connectivity probe
    db_info: dict = {}
    try:
        from sqlalchemy import text
        from db.database import engine
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        db_info = {"status": "healthy"}
    except Exception as exc:
        db_info = {"status": "unhealthy", "error": str(exc)}
    db_status = ComponentStatus(status=db_info["status"], details=db_info)

    # Redis
    redis_info: dict = {}
    try:
        import redis as redis_lib
        r = redis_lib.from_url(settings.REDIS_URL, socket_timeout=2)
        r.ping()
        redis_info = {"status": "healthy"}
    except Exception as exc:
        redis_info = {"status": "unhealthy", "error": str(exc)}
    redis_status = ComponentStatus(status=redis_info["status"], details=redis_info)

    overall = "healthy"
    if any(s.status != "healthy" for s in [vdb_status, db_status]):
        overall = "degraded"

    return StatusResponse(
        status=overall,
        database=db_status,
        vector_db=vdb_status,
        llm=llm_status,
        redis=redis_status,
    )


@router.get("/metrics")
async def metrics():
    """Basic performance metrics."""
    vdb = qdrant_health()
    return {
        "uptime_seconds": round(time.time() - _start_time, 2),
        "vectors_count": vdb.get("vectors_count", 0),
        "points_count": vdb.get("points_count", 0),
    }
