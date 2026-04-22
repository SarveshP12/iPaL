"""
Authentication API routes — register, login, and user profile.
"""

import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db.database import get_db
from models.models import User
from schemas.schemas import UserCreate, UserResponse, TokenResponse
from services.auth_service import AuthService, get_current_user
from config.settings import settings

router = APIRouter(prefix="/api/auth", tags=["Authentication"])
auth = AuthService()


@router.post("/register", response_model=UserResponse, status_code=201)
async def register(request: UserCreate, db: AsyncSession = Depends(get_db)):
    """Register a new user."""
    # Check if username or email already exists
    existing = await db.execute(
        select(User).where((User.username == request.username) | (User.email == request.email))
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Username or email already exists")

    user = User(
        id=uuid.uuid4(),
        username=request.username,
        email=request.email,
        hashed_password=auth.hash_password(request.password),
        role="user",
    )
    db.add(user)
    await db.flush()

    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        role=user.role,
        is_active=True,
        created_at=datetime.now(timezone.utc),
    )


@router.post("/login", response_model=TokenResponse)
async def login(username: str, password: str, db: AsyncSession = Depends(get_db)):
    """Authenticate and return a JWT token."""
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalar_one_or_none()

    if not user or not auth.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not user.is_active:
        raise HTTPException(status_code=403, detail="Account is deactivated")

    token = auth.create_access_token(str(user.id), user.role)
    return TokenResponse(
        access_token=token,
        expires_in=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )


@router.get("/me", response_model=UserResponse)
async def get_profile(user: User = Depends(get_current_user)):
    """Get the current authenticated user's profile."""
    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        role=user.role,
        is_active=user.is_active,
        created_at=user.created_at,
    )
