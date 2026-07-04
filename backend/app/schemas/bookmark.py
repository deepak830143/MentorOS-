from datetime import datetime

from pydantic import BaseModel


# ==========================================================
# Create Bookmark
# ==========================================================

class BookmarkCreate(BaseModel):

    notification_id: int


# ==========================================================
# Bookmark Response
# ==========================================================

class BookmarkResponse(BaseModel):

    id: int

    user_id: int

    notification_id: int

    created_at: datetime

    class Config:

        from_attributes = True


# ==========================================================
# Saved Notification Response
# ==========================================================

class SavedNotificationResponse(BaseModel):

    id: int

    exam_name: str

    notification_no: str | None = None

    organization: str

    category: str

    vacancies: int | None = None

    application_end: str | None = None

    pdf_url: str | None = None

    ai_summary: str | None = None