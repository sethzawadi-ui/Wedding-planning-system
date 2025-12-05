from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from lib.models.base import Base


class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120))
    phone = Column(String(20))
    rsvp = Column(Boolean, default=False)

    event_id = Column(Integer, ForeignKey("events.id", ondelete="SET NULL"))
    event = relationship("Event", back_populates="guests")

    def __init__(self, name, email=None, phone=None, rsvp=False, event_id=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.rsvp = rsvp
        self.event_id = event_id

    def __repr__(self):
        return f"<Guest {self.name} | RSVP: {self.rsvp}>"
