# SQLAlchemy engine + session setup will be added in future commits.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Placeholder engine - will be improved later
DATABASE_URL = "sqlite:///wedding_planner.db"

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

# global session reference
session = Session()
