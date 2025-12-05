from sqlalchemy import Column, Integer, String
from lib.models.base import Base
import hashlib

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    role = Column(String(20), default="Guest")  # Admin, Planner, Bride, Groom, Guest

    def __init__(self, username, password, role="Guest"):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.role = role

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

    def __repr__(self):
        return f"<User {self.username} | Role: {self.role}>"
