from sqlalchemy import Column, DateTime, String, Integer, Boolean, Float, func
from database._db import Base
from service.util_service import *

class Setting(Base):
    __tablename__ = 'setting'

    id                  = Column(Integer, primary_key=True)
    key                 = Column(String(length=100))
    value               = Column(String(length=250)) 

    def __init__(self, key, value):
        self.key   = key
        self.value = value

    def json(self):
        return get_props(self)
