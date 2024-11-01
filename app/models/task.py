from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from sqlalchemy import String

class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[str | None] = mapped_column(String, nullable=True)

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            description=self.description,
            completed_at=self.completed_at
        )
