import random
import time
import json
from database._db import session
from service.db_service import *
from service.world_service import *
from service.util_service import *
from service.navigation_service import *

def draw_new_target(ecxlude_x, exclude_y, tiles_x, tiles_y):    
    new_x = random.choice([i for i in range(1,tiles_x) if i not in ecxlude_x])
    new_y = random.choice([i for i in range(1,tiles_y) if i not in exclude_y])
    return {"x" : new_x, "y": new_y }

def move_objects(movement):
    try:
        for idx_mov, mov in enumerate(movement[:]):
            for idx_dir, dir in enumerate(mov.path["dir"][:]):  #use a copy of the list [:] to remove 
                if int(mov["object"]["next_move_monotic"]) < time.monotonic():
                    del movement[idx_mov]["path"]["dir"][idx_dir] #del old move
                    movement[idx_mov + 1]["object"].next_move_monotonic = time.monotonic() + movement[idx_mov + 1]["object"].speed_monotic #when next move can be send to client                    
                    world_object = get_world_object(mov.id) #get world object from db for quick update x and y
                    world_object.x = mov["object"]["x"]
                    world_object.y = mov["object"]["y"]
                    world_object.moving = True
                    map = get_map_by_id(world_object.map_id)
                    
                    if to_bool(mov["target_x"]) != True and to_bool(mov["target_y"]) != True: #del object info if it reached the target (clear the buffer)
                        del movement[idx_mov]
                        world_object.moving = False
                        world_object.next_move_monotonic = time.monotonic() + world_object.idle_time_monotonic

                    update_world_object(world_object)
                    yield json.dumps({"map_name": map.name, "object_id": mov.id, "dir": dir})
    except Exception as c:
        print(c) #Todo logs

def generate_path(object, obstacle_x, obstacle_y):
    if (object.x == 0 or object.y == 0):
        return {"error": 0}
    path = None # TODO: A* to be implemented -> use path finding algorith (A*) and return directions (direction.py) return array of directions;
    #path = {"dir": dir, "x": target_x, "y": target_y } ##dir->direction

    return {} # {"object": object, "path": path, "target_x": true, "target_y": false} # Object should have new x and y set up 




