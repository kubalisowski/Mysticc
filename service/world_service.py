import json
from database._db import session
from database.model.world_object import WorldObject
from database.model.setting import Setting
from database.model.map import Map
from database.model.world_object_path import WorldObjectPath
from service.util_service import *
from sqlalchemy import asc

### MAP ###
def get_all_maps():
    return session.query(Map).all()

def get_map_by_id(map_id):
    return session.query(Map).filter_by(id=map_id).first()

def get_map_by_name(map_name):
    return session.query(Map).filter_by(name=map_name).first()

### WORLD OBJECT ###
def get_world_object(id):
    return session.query(WorldObject).filter_by(id=id).first()

def get_world_objects():
    return list(session.query(WorldObject)).all()

def get_world_objects(map_id=0, static=False, moving=False):
    return list(session.query(WorldObject).filter_by(map_id=map_id, static=static, moving=moving)).all()

def update_world_object(object):
    session.query(WorldObject).filter_by(id=object.id).update(object.json()) # not working? use get_props(object) instead of object.json()
    session.commit()

### WORLD OBJECT PATH ###
def get_world_object_path():
    return session.query(WorldObjectPath).all()

def get_world_object_path(map_id):
    return session.query(WorldObjectPath).filter_by(map_id=map_id)

def get_world_object_path(id):
    return session.query(WorldObjectPath).filter_by(id=id)

def get_world_object_path_groupby(map_id=True, object_id=True):
    return session.query(WorldObjectPath).group_by(WorldObjectPath.map_id).group_by(WorldObjectPath.object_id).order_by(asc(WorldObjectPath.order)).all()

def delete_world_object_path(id):
    session.query(WorldObjectPath).filter(id=id).delete()
    session.commit()

def get_world_object_path():
    return session.query(WorldObjectPath).all()


