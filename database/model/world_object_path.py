from sqlalchemy import Column, DateTime, String, Integer, Boolean, func
from database._db import Base
from service.util_service import *

class WorldObjectPath(Base):
    __tablename__ = 'world_object_path'

    id           = Column(Integer, primary_key=True)
    map_id       = Column(Integer)
    object_id    = Column(Integer)    
    direction    = Column(Integer)
    target_x     = Column(Boolean)
    target_y     = Column(Boolean)
    order        = Column(Integer)

    def json(self):
        return get_props(self)


class WorldObjectPathClient:
    def __init__(self, object_id, direction, x, y, target_x, target_y):
        self.object_id  = object_id
        self.direction  = direction
        self.x          = x
        self.y          = y
        self.target_x   = target_x
        self.target_y   = target_y
    
    def json(self):
        return get_props(self)