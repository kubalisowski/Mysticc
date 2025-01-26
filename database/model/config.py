from sqlalchemy import Column, DateTime, String, Integer, Boolean, Float, func
from database._db import Base
from service.util_service import *

class Config(Base):
    __tablename__ = 'config'

    id                  = Column(Integer, primary_key=True)
    type                = Column(String(length=100))
    name                = Column(String(length=100))
    value               = Column(String(length=250)) 

    def json(self):
        return get_props(self)
