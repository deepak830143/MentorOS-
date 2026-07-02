from fastapi import FastAPI

from app.api.auth_routes import router as auth_router
from app.api.user_routes import router as user_router
from app.core.config import settings
from app.db.base import Base
from app.db.database import engine

# Import all models
from app.models.user import User

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# Register Routers
app.include_router(auth_router)
app.include_router(user_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to MentorOS 🚀",
        "version": settings.APP_VERSION,
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }