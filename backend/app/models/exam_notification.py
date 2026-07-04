from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Date,
    DateTime,
)
from sqlalchemy.sql import func

from app.db.base import Base


class ExamNotification(Base):
    __tablename__ = "exam_notifications"

    id = Column(Integer, primary_key=True, index=True)

    source = Column(
        String(50),
        nullable=False,
    )

    organization = Column(
        String(100),
        nullable=False,
    )

    exam_name = Column(
        String(255),
        nullable=False,
    )

    notification_no = Column(
        String(100),
        nullable=True,
    )

    title = Column(
        String(500),
        nullable=False,
    )

    notification_hash = Column(
        String(64),
        unique=True,
        nullable=False,
        index=True,
    )

    category = Column(
        String(100),
        nullable=False,
    )

    status = Column(
        String(50),
        default="OPEN",
    )

    vacancies = Column(
        Integer,
        nullable=True,
    )

    # CHANGED FROM String(255) TO Text
    qualification = Column(
        Text,
        nullable=True,
    )

    age_limit = Column(
        String(100),
        nullable=True,
    )

    salary = Column(
        String(255),
        nullable=True,
    )

    application_start = Column(
        Date,
        nullable=True,
    )

    application_end = Column(
        Date,
        nullable=True,
    )

    exam_date = Column(
        Date,
        nullable=True,
    )

    pdf_url = Column(
        Text,
        nullable=True,
    )

    apply_url = Column(
        Text,
        nullable=True,
    )

    official_url = Column(
        Text,
        nullable=True,
    )

    description = Column(
        Text,
        nullable=True,
    )

    ai_summary = Column(
        Text,
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )