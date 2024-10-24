from database._db import session
from database.model.game_object import GameObject

def get_all_game_objects():
    return session.query(GameObject).all()

def get_all_game_objects_json():
    game_objects = get_all_game_objects()
    return [obj.json() for obj in game_objects]





