import random
import time
from database.model.enum import Directions
from database.model.world_object import *
from database.model.world_object_path import *
from service.db_service import *
from service.world_service import *
from service.util_service import *
from service.world_service import *
from database._db import session

def draw_new_target(ecxlude_x, exclude_y, tiles_x, tiles_y):
    new_x = random.choice([i for i in range(1,tiles_x) if i not in ecxlude_x])
    new_y = random.choice([i for i in range(1,tiles_y) if i not in exclude_y])
    return {"x" : new_x, "y": new_y }

def object_path_algorithm(object, obstacle_x, obstacle_y):
    if (object.x == 0 or object.y == 0):
        return {"error": 0}
    path = None # TODO: A* to be implemented -> use path finding algorith (A*) and return directions (direction.py) return array of directions;
    #path = {"dir": dir, "x": target_x, "y": target_y } ##dir->direction

    return [] #list of WorldObjectPathClient

def get_object_path():
    path_for_map = {}
    for map in get_all_maps():
        static     = get_world_objects(map_id=map.id, static=True)
        idle       = filter(lambda x: x.last_move_monotonic + x.idle_time_tics < time.monotonic(), get_world_objects(static=False, moving=False))
        to_move    = filter(lambda x: x.last_move_monotonic + x.idle_time_tics > time.monotonic(), get_world_objects(static=False, moving=False))
        obstacles  = static + idle
        obstacle_x = list(filter(lambda obj: obj.x, obstacles))
        obstacle_y = list(filter(lambda obj: obj.y, obstacles))

        for object in to_move:
            path_for_map[map.name] = object_path_algorithm(object, obstacle_x, obstacle_y)
            obstacle_x.append(object.x)
            obstacle_y.append(object.y)

    return path_for_map

def create_object_path():
    for map_name, world_object_path in get_object_path():
        session.add_all(world_object_path)
        session.commit()

def set_object_new_position(world_object, path):
    match path.direction:
        case Directions.UP:
            world_object.y += 1
        case Directions.DOWN:
            world_object.y -= 1
        case Directions.RIGHT:
            world_object.x += 1
        case Directions.RIGHT:
            world_object.x -= 1

def get_next_moves():
    next_moves = {}
    for map in get_all_maps():
        moves = []
        for group_by_map_id in get_world_object_path_groupby():
            for group_by_object_id in group_by_map_id: # group_by map_id
                for world_object_path in group_by_object_id: # group_by object_id
                    moves.append(world_object_path[0]) # first row=> next move
        next_moves[map.id] = moves

def move_objects():
    try:
        for map_id, paths in get_next_moves():
            for path in paths:
                world_object = get_world_object(path.object_id)
                if (time.monotonic() + world_object.next_move_monotic > time.monotonic()):                    
                    if path.target_x and path.target_y: #target position
                        world_object.direction = None
                        world_object.moving    = False
                        world_object.last_move_monotic = time.monotonic()
                        world_object.next_move_monotic = None
                    else: #next position, moving
                        set_object_new_position(world_object)
                        world_object.moving = True
                        world_object.last_move_monotic = None
                        world_object.next_move_monotic = time.monotonic() + world_object.speed_tics

                    update_world_object(world_object)
                    delete_world_object_path(path.id)

                    client_paths = []
                    client_paths.append(WorldObjectPathClient(world_object.object_id, path.direction, world_object.x, world_object.y, path.target_x, path.target_y))
            
            yield { get_map_by_id(map_id).name: client_paths } #to controller
    except Exception as c:
        print(c) #Todo logs





