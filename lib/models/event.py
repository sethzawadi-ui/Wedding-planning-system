from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy.orm import relationship
from lib.models.base import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    date = Column(Date)
    time = Column(Time)
    location = Column(String(100))

    guests = relationship("Guest", back_populates="event", cascade="all, delete")

    tasks = relationship("Task", back_populates="event", cascade="all, delete")

    def __init__(self, title, date=None, time=None, location=None):
        self.title = title
        self.date = date
        self.time = time
        self.location = location

    def __repr__(self):
        return f"<Event {self.title} on {self.date}>"
