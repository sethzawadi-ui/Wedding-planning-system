from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.models.base import Base

class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    rsvp_status = Column(String(20), default="Pending")  # Pending, Accepted, Declined
    event_id = Column(Integer, ForeignKey("events.id"), nullable=True)

    event = relationship("Event", back_populates="guests")

    def __repr__(self):
        return f"<Guest {self.name} | RSVP: {self.rsvp_status}>"
