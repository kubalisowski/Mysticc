from database._db import session
from database.model.world_object import WorldObject
from database.model.setting import Setting
from database.model.map import Map
from util_service import *

### MAP ###
def get_all_maps():
    return session.query(Map).all()

def get_map_by_id(map_id):
    return session.query(Map).filter_by(id=map_id).first()

def get_map_by_name(map_name):
    return session.query(Map).filter_by(name=map_name).first()

### GAME OBJECT ###
def get_world_object(id):
    return session.query(WorldObject).filter_by(id=id).first()

def get_world_objects():
    return list(session.query(WorldObject)).all()

def get_world_objects(map_id=0, static=False, moving=False):
    return list(session.query(WorldObject).filter_by(map_id=map_id, static=static, moving=moving)).all()

def update_world_object(object):
    session.query(WorldObject).filter(WorldObject.id == object.id).update(object.json()) # not working? use get_props(object) instead of object.json()
    session.commit()




        




