from sqlalchemy import Column, Integer, String, DateTime

from src.config.db.inventory import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    name = Column(String(45), unique=True, nullable=False)
    quantity = Column(Integer)
    description = Column(String(255))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
