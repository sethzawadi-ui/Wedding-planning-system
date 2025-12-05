from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import relationship
from .base import Base
from .expense import Expense

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True)
    total_budget = Column(Float, default=0.0)

    # Relationship to expenses
    expenses = relationship("Expense", back_populates="budget", cascade="all, delete-orphan")

    def add_expense(self, name, amount):
        expense = Expense(name=name, amount=amount, budget=self)
        self.expenses.append(expense)
        return expense

    def calculate_remaining(self):
        total_expenses = sum(exp.amount for exp in self.expenses)
        return self.total_budget - total_expenses

    def __repr__(self):
        return f"<Budget(total_budget={self.total_budget}, remaining={self.calculate_remaining()})>"
