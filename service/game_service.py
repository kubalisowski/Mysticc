from database._db import session
from database.model.game_object import GameObject
from database.model.map import Map

### MAP ###
def get_map_by_name(map_name):
    return session.query(Map).filter_by(name=map_name).first()

### GAME OBJECT ###
def get_all_game_objects():
    return session.query(GameObject).all()

def get_all_game_objects_json():
    game_objects = get_all_game_objects()
    return [obj.json() for obj in game_objects]




