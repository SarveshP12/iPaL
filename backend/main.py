"""
iPaL Backend — FastAPI Application Entry Point

Initialises the app, registers routes, configures middleware,
and runs startup/shutdown lifecycle hooks.
"""

import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from config.settings import settings
from config.logging_config import setup_logging, get_logger
from db.qdrant_setup import init_qdrant

# ── Logging ──────────────────────────────────────
setup_logging()
logger = get_logger("ipal")


# ── Lifecycle ────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown hooks."""
    logger.info("Starting iPaL backend", version=settings.APP_VERSION)

    # Initialise Qdrant collection
    try:
        init_qdrant()
        logger.info("Qdrant initialised")
    except Exception as exc:
        logger.warning("Qdrant init failed (will retry on first use)", error=str(exc))

    # Create database tables if needed
    try:
        from db.database import engine, Base
        from models.models import User, ChatSession, ChatMessage, Document, IngestionJob  # noqa: F401
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Database tables ensured")
    except Exception as exc:
        logger.warning("Database table creation failed", error=str(exc))

    yield

    logger.info("Shutting down iPaL backend")


# ── App factory ──────────────────────────────────
app = FastAPI(
    title="iPaL — ICICI Bank Intelligent Personal Assistant",
    description="RAG-powered chatbot API for ICICI Bank customer queries",
    version=settings.APP_VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# ── CORS ─────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Request timing middleware ────────────────────
@app.middleware("http")
async def add_timing_header(request: Request, call_next):
    start = time.perf_counter()
    response: Response = await call_next(request)
    elapsed = round((time.perf_counter() - start) * 1000, 2)
    response.headers["X-Response-Time-Ms"] = str(elapsed)
    return response


# ── Input sanitisation middleware ────────────────
@app.middleware("http")
async def sanitise_inputs(request: Request, call_next):
    """Basic input validation — reject excessively large payloads."""
    content_length = request.headers.get("content-length")
    if content_length and int(content_length) > 10 * 1024 * 1024:  # 10 MB
        from fastapi.responses import JSONResponse
        return JSONResponse(status_code=413, content={"detail": "Payload too large"})
    return await call_next(request)


# ── Register routers ────────────────────────────
from routes.chat import router as chat_router
from routes.health import router as health_router
from routes.admin import router as admin_router
from routes.auth import router as auth_router

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(admin_router)
app.include_router(auth_router)


# ── Root endpoint ────────────────────────────────
@app.get("/", tags=["Root"])
async def root():
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "health": "/api/health",
    }
