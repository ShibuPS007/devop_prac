from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from database import Base


class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    a = Column(Float)
    b = Column(Float)
    operation = Column(String)
    result = Column(Float)
    created_at = Column(DateTime, default=datetime.now)