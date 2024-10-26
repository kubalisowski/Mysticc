from sqlalchemy import Column, DateTime, String, Integer, Boolean, Float, func
from database._db import Base

class MoveObject(Base):
    __tablename__ = 'move_object'

    id             = Column(Integer, primary_key=True)
    game_object_id = Column(Integer)
    x_position     = Column(Integer)
    y_position     = Column(Integer)
    direction      = Column(Integer)
    interval       = Column(Float)
    destination    = Column(Boolean)

    def json(self):
        return {
            'id'             : self.id,
            'game_object_id' : self.game_object_id,    
            'x_position'     : self.x_position,    
            'y_position'     : self.y_position, 
            'direction'      : self.direction,
            'interval'       : self.interval,
            'destination'    : self.destination,
        }