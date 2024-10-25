from sqlalchemy import Column, DateTime, String, Integer, Boolean, func
from database._db import Base

class Map(Base):
    __tablename__ = 'map'

    id           = Column(Integer, primary_key=True)
    name         = Column(String(length=100))
    img_src      = Column(String(length=200))
    width_tile   = Column(Integer)
    height_tile  = Column(Integer)
    
    def json(self):
        return {
            'id'     : self.id,
            'name'   : self.name,    
            'img_src': self.img_src,    
            'width'  : self.width, 
            'height' : self.height,
        }