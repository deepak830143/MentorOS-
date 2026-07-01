from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-Powered Competitive Exam Operating System",
    version=settings.APP_VERSION
)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME} 🚀",
        "version": settings.APP_VERSION,
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": settings.APP_NAME
    }