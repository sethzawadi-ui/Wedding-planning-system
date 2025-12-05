from sqlalchemy import Column, Integer, String, Float
from lib.models.base import Base


class Budget(Base):
    __tablename__ = "budget"

    id = Column(Integer, primary_key=True)
    category = Column(String(50), nullable=False)     # Catering, Venue, Decor, etc.
    amount = Column(Float, nullable=False)            # Spent amount
    notes = Column(String(200))

    def __init__(self, category, amount, notes=None):
        self.category = category
        self.amount = amount
        self.notes = notes

    def __repr__(self):
        return f"<Budget {self.category}: {self.amount}>"
