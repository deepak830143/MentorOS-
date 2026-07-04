from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class ExamNotificationBase(BaseModel):
    source: str
    organization: str
    exam_name: str
    notification_no: Optional[str] = None
    title: str

    # IMPORTANT
    notification_hash: Optional[str] = None

    category: str
    status: str = "OPEN"

    vacancies: Optional[int] = None
    qualification: Optional[str] = None
    age_limit: Optional[str] = None
    salary: Optional[str] = None

    application_start: Optional[date] = None
    application_end: Optional[date] = None
    exam_date: Optional[date] = None

    pdf_url: Optional[str] = None
    apply_url: Optional[str] = None
    official_url: Optional[str] = None

    description: Optional[str] = None
    ai_summary: Optional[str] = None


class ExamNotificationCreate(ExamNotificationBase):
    pass


class ExamNotificationResponse(ExamNotificationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True