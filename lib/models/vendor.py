from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from lib.models.base import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    service_type = Column(String(50), nullable=False)
    cost = Column(Float, nullable=False)
    is_booked = Column(Boolean, default=False)

    # Foreign key to event
    event_id = Column(Integer, ForeignKey("events.id"), nullable=True)
    event = relationship("Event", back_populates="vendors")

    def __repr__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"<Vendor {self.name} ({self.service_type}) - {status}>"
