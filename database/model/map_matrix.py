from sqlalchemy import Column, DateTime, String, Integer, Boolean, func
from database._db import Base

class MapMatrix(Base):
    __tablename__ = 'map_matrix'

    id        = Column(Integer, primary_key=True)
    map_id    = Column(Integer)
    tile_type = Column(Integer)

    
    def json(self):
        return {
            'id'       : self.id,
            'map_id'   : self.map_id,    
            'tile_type': self.tile_type,
        }
    

