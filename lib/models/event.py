from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy.orm import relationship
from lib.models.base import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    location = Column(String(120), nullable=False)

    # Relationship to vendors
    vendors = relationship("Vendor", back_populates="event")

    def __repr__(self):
        return f"<Event {self.name} on {self.date} at {self.time}>"
