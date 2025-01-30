from sqlalchemy import Column, DateTime, String, Integer, Boolean, func
from database._db import Base
from service.util_service import *

class WorldObjectPath(Base):
    __tablename__ = 'world_object_path'

    id           = Column(Integer, primary_key=True)
    object_id    = Column(Integer)
    direction    = Column(Integer)
    target_x     = Column(Boolean)
    target_y     = Column(Boolean)
    order        = Column(Integer)

    def json(self):
        return get_props(self)
    
