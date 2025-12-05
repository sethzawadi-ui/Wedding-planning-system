from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    budget_id = Column(Integer, ForeignKey("budgets.id"))

    # Relationship to parent budget
    budget = relationship("Budget", back_populates="expenses")

    def __repr__(self):
        return f"<Expense(name={self.name}, amount={self.amount})>"
