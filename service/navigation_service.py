import random
import time
from service.db_service import *
from service.world_service import *
from service.util_service import *
from service.world_service import *

def draw_new_target(ecxlude_x, exclude_y, tiles_x, tiles_y):
    new_x = random.choice([i for i in range(1,tiles_x) if i not in ecxlude_x])
    new_y = random.choice([i for i in range(1,tiles_y) if i not in exclude_y])
    return {"x" : new_x, "y": new_y }

def generate_path_for_object(object, obstacle_x, obstacle_y):
    if (object.x == 0 or object.y == 0):
        return {"error": 0}
    path = None # TODO: A* to be implemented -> use path finding algorith (A*) and return directions (direction.py) return array of directions;
    #path = {"dir": dir, "x": target_x, "y": target_y } ##dir->direction

    return [] #list of WorldObjectPath

def get_objects_path():
    for map in get_all_maps():
        static     = get_world_objects(map_id=map.id, static=True, moving=False)
        idle       = filter(lambda x: time.monotonic() + x.next_move_monotonic > time.monotonic(), get_world_objects(static=False, moving=False))
        to_move    = filter(lambda x: time.monotonic() + x.next_move_monotonic < time.monotonic(), get_world_objects(static=False, moving=False))
        obstacles  = static + idle
        obstacle_x = filter(lambda obj: obj.x, obstacles)
        obstacle_y = filter(lambda obj: obj.y, obstacles)

        paths = {}
        for object in to_move:
            path = generate_path_for_object(object, obstacle_x, obstacle_y)
            paths.append(path)

    return paths

def move_objects(object_moves):
    try:
        for idx_mov, mov in enumerate(object_moves[:]):
            for idx_dir, dir in enumerate(mov.path["dir"][:]):  #use a copy of the list [:] to remove 
                if int(mov["object"]["next_move_monotic"]) < time.monotonic():
                    del object_moves[idx_mov]["path"]["dir"][idx_dir] #del old move
                    object_moves[idx_mov + 1]["object"].next_move_monotonic = time.monotonic() + object_moves[idx_mov + 1]["object"].speed_monotic #when next move can be send to client                    
                    world_object = get_world_object(mov.id) #get world object from db for quick update x and y
                    world_object.x = mov["object"]["x"]
                    world_object.y = mov["object"]["y"]
                    world_object.moving = True
                    map = get_map_by_id(world_object.map_id)
                    
                    if to_bool(mov["target_x"]) != True and to_bool(mov["target_y"]) != True: #del object info if it reached the target (clear the buffer)
                        del object_moves[idx_mov]
                        world_object.moving = False
                        world_object.next_move_monotonic = time.monotonic() + world_object.idle_time_monotonic

                    update_world_object(world_object)
                    yield {"map_name": map.name, "object_id": mov.id, "dir": dir}
    except Exception as c:
        print(c) #Todo logs





