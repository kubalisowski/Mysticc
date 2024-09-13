from sqlalchemy import Column, DateTime, String, Integer, Boolean, func
from database._db import Base

class Test(Base):
   __tablename__ = 'test'
   id = Column(Integer, primary_key=True)
   txt = Column(String(length=100))
    