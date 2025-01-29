from database._db import session
from database.model.world_object import WorldObject
from database.model.setting import Setting
from database.model.map import Map
from navigation_service import *
from util_service import *
import time
import json

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

def get_world_objects(map_id=None):
    return list(session.query(WorldObject).filter_by(map_id=map_id)).all()

def get_world_objects(static, moving):
    return list(session.query(WorldObject).filter_by(static=static, moving=moving)).all()

def update_world_object(object):
    session.query(WorldObject).filter(WorldObject.id == object.id).update(object.json()) # not working? use get_props(object) instead of object.json()
    session.commit()


### MOVE ###
def get_path():
    maps = {}
    for map in get_all_maps():
        maps[map.Id] = map

    static     = get_world_objects(static=True, moving=False)
    idle       = filter(lambda x: x.next_move_monotonic > time.monotonic(), get_world_objects(static=False, moving=False))
    to_move    = filter(lambda x: x.next_move_monotonic < time.monotonic(), get_world_objects(static=False, moving=False))
    obstacles  = static + idle
    obstacle_x = filter(lambda obj: obj.x, obstacles)
    obstacle_y = filter(lambda obj: obj.y, obstacles)

    paths = {}
    for object in to_move:
        path = generate_path(object, obstacle_x, obstacle_y)
        obstacle_x.append()
        obstacle_y.append()
        paths[object] = path

    return paths

        




