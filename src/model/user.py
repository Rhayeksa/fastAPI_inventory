from sqlalchemy import Column, Integer, String, DateTime

from src.config.db.inventory import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    username = Column(String(45), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
