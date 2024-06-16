from sqlalchemy import Column, DateTime, String, Integer, Boolean, func
from database._db import Base

class Map(Base):
    __tablename__ = 'map'

    id      = Column(Integer, primary_key=True)
    name    = Column(String(length=100))
    width   = Column(Integer)
    height  = Column(Integer)
    
