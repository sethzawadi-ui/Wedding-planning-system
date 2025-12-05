# Database engine and session creation using SQLAlchemy ORM

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models.base import Base

# SQLite database for CLI app
DATABASE_URL = "sqlite:///wedding_planner.db"

# echo=True is useful for debugging SQL queries
engine = create_engine(DATABASE_URL, echo=False)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Global session instance
session = Session()


def init_db():
    """Creates all tables defined in the ORM models."""
    Base.metadata.create_all(engine)
