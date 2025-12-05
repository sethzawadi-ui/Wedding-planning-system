from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from lib.models.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    deadline = Column(Date)
    completed = Column(Boolean, default=False)

    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("Event", back_populates="tasks")

    def __init__(self, title, deadline=None, completed=False, event_id=None):
        self.title = title
        self.deadline = deadline
        self.completed = completed
        self.event_id = event_id

    def __repr__(self):
        return f"<Task {self.title} | Completed: {self.completed}>"
