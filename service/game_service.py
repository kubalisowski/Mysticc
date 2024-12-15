from database._db import session
from database.model.game_object import GameObject
from database.model.map import Map
from navigation_service import *
import time

### MAP ###
def get_all_maps():
    return session.query(Map).all()

def get_map_by_id(map_id):
    return session.query(Map).filter_by(id=map_id).first()

def get_map_by_name(map_name):
    return session.query(Map).filter_by(name=map_name).first()



### GAME OBJECT ###
def get_game_objects():
    return list(session.query(GameObject)).all()

def get_game_objects(map_id=None):
    return list(session.query(GameObject).filter_by(map_id=map_id)).all()

def get_game_objects(static, moving):
    return list(session.query(GameObject).filter_by(static=static, moving=moving)).all()

# obsolete but might be in use
def get_all_game_objects_json():
    game_objects = get_game_objects()
    return [obj.json() for obj in game_objects]
######

def get_game_objects_json(game_objects):
    return [obj.json() for obj in game_objects]


### MOVE ###
def move_objects():
    maps = {}
    for map in get_all_maps():
        maps[map.Id] = map

    static     = get_game_objects(static=True, moving=False)
    idle       = filter(lambda x: x.idle_stop_monotonic > time.monotonic(), get_game_objects(static=False, moving=False))
    to_move    = filter(lambda x: x.idle_stop_monotonic < time.monotonic(), get_game_objects(static=False, moving=False))
    obstacles  = static + idle
    obstacle_x = filter(lambda obj: obj.x, obstacles)
    obstacle_y = filter(lambda obj: obj.y, obstacles)

    paths = {}
    for object in to_move:
        path = generate_path(object, obstacle_x, obstacle_y)
        obstacle_x.append(path["target_x"])
        obstacle_y.append(path["target_y"])
        paths[object.id] = path

    return paths

        




