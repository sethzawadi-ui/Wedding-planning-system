from sqlalchemy import Column, Integer, String, Boolean
from lib.models.base import Base


class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    service_type = Column(String(50), nullable=False)  # Catering, DJ, Photography
    phone = Column(String(20))
    booked = Column(Boolean, default=False)

    def __init__(self, name, service_type, phone=None, booked=False):
        self.name = name
        self.service_type = service_type
        self.phone = phone
        self.booked = booked

    def __repr__(self):
        return f"<Vendor {self.name} ({self.service_type}) | Booked: {self.booked}>"
