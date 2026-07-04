from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.base import Base
from app.db.database import engine

# ==========================================================
# Import Models
# ==========================================================

from app.models.user import User
from app.models.exam_notification import ExamNotification
from app.models.bookmark import Bookmark

# ==========================================================
# Import Routers
# ==========================================================

from app.api.auth_routes import router as auth_router
from app.api.user_routes import router as user_router
from app.api.exam_notification_routes import (
    router as notification_router,
)
from app.api.dashboard_routes import (
    router as dashboard_router,
)
from app.api.bookmark_routes import (
    router as bookmark_router,
)

# ==========================================================
# Import Scheduler
# ==========================================================

from app.scheduler.scheduler import start_scheduler

# ==========================================================
# Create Database Tables
# ==========================================================

Base.metadata.create_all(bind=engine)

# ==========================================================
# FastAPI Application
# ==========================================================

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# ==========================================================
# CORS Configuration
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================================
# Startup Event
# ==========================================================

@app.on_event("startup")
def startup_event():
    start_scheduler()

# ==========================================================
# Register Routers
# ==========================================================

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(notification_router)
app.include_router(dashboard_router)
app.include_router(bookmark_router)

# ==========================================================
# Root Endpoint
# ==========================================================

@app.get("/")
def root():
    return {
        "message": "Welcome to MentorOS 🚀",
        "status": "Running",
        "version": settings.APP_VERSION,
    }

# ==========================================================
# Health Check
# ==========================================================

@app.get("/health")
def health():
    return {
        "status": "Healthy",
    }