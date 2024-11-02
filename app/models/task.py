from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from sqlalchemy import String, Boolean

class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[str | None] = mapped_column(String, nullable=True)
    is_complete: Mapped[bool] = mapped_column(Boolean, default=False)

    def to_dict(self):
        response = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_complete": self.completed_at is not None
        }
        if self.completed_at is not None:
            response["completed_at"] = self.completed_at
        
        return response
