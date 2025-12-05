# User ORM Model
# Handles secure storage of user credentials and role-based access

from sqlalchemy import Column, Integer, String
from lib.models.base import Base
import bcrypt


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    password_hash = Column(String(200), nullable=False)
    role = Column(String(20), nullable=False)  # Admin, Planner, Bride, Groom, Guest

    def __init__(self, username, password, role):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.role = role

    # --------- PASSWORD HASHING ---------

    def hash_password(self, password: str) -> str:
        """Hashes password using bcrypt."""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()

    def verify_password(self, password: str) -> bool:
        """Verifies password using bcrypt."""
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())

    # --------- STRING REPRESENTATION ---------

    def __repr__(self):
        return f"<User {self.username} ({self.role})>"

