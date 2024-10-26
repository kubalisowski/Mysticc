from sqlalchemy import Column, DateTime, String, Integer, Boolean, func
from database._db import Base


class MapObject(Base):
    __tablename__ = 'map_object'

    id             = Column(Integer, primary_key=True),
    map_id         = Column(Integer),
    game_object_id = Column(Integer),
    x_position     = Column(Integer),
    y_position     = Column(Integer),
    move           = Column(Boolean)
    
    def json(self):
        return {
            'id'            : self.id,
            'map_id'        : self.map_id,
            'game_object_id': self.game_object_id,  
            'x_position'    : self.x_position,
            'y_position'    : self.y_position,
            'move'          : self.move
        }




