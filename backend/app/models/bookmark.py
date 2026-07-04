from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    notification_id = Column(
        Integer,
        ForeignKey(
            "exam_notifications.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    # -------------------------------
    # Relationships
    # -------------------------------

    user = relationship(
        "User",
        backref="bookmarks",
    )

    notification = relationship(
        "ExamNotification",
        backref="bookmarks",
    )