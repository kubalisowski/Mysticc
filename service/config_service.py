
from config import *
from database._db import session
from database.model.setting import Setting

### CONFIG ###
def get_client_config():
    return {
        'SCREEN': SCREEN,
        'SCROLL_INTERVAL_MS': SCROLL_INTERVAL_MS,
        'SCROLL_PIXEL': SCROLL_PIXEL,
        'TILE_WIDTH': TILE_WIDTH,
        'TILE_HEIGHT': TILE_HEIGHT,
        'MAP_NAME': MAP_NAME,
        'MAP_CONTAINER_WIDTH': MAP_CONTAINER_WIDTH,
        'MAP_CONTAINER_HEIGHT': MAP_CONTAINER_HEIGHT,
        'DIRS': DIRS
    }

### SETTING ###
def get_setting_type():
    return session.query(Setting).all()

def get_setting_type(type):
    return session.query(Setting).filter_by(type=type).all()

def setting(name):
    return session.query(Setting).filter_by(name=name).first()