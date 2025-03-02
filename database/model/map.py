from sqlalchemy import Column, DateTime, String, Integer, Boolean, func
from database._db import Base
from service.util_service import *

class Map(Base):
    __tablename__ = 'map'

    id           = Column(Integer, primary_key=True)
    name         = Column(String(length=100))
    img_src      = Column(String(length=200))
    width_tile   = Column(Integer)
    height_tile  = Column(Integer)
    grid         = Column(String(length=2000))
    grid_row     = Column(Integer)
    grid_col     = Column(Integer)
    
    def json(self):
        return get_props(self)

    # def json(self):
    #     return {
    #         'id'          : self.id,
    #         'name'        : self.name,    
    #         'img_src'     : self.img_src,    
    #         'width_tile'  : self.width_tile, 
    #         'height_tile' : self.height_tile,
    #     }