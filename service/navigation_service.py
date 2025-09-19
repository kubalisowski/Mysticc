import random
import time
from database.model.enum              import Directions
from database.model.world_object      import *
from database.model.world_object_path import *
from service.db_service               import *
from service.world_service            import *
from service.util_service             import *
from service.world_service            import *
from service.path_algoritm            import *
from database._db                     import session

def draw_new_target(ecxlude_x, exclude_y, grid_col, grid_row):
    new_x = random.choice([i for i in range(1, grid_col) if i not in ecxlude_x])
    new_y = random.choice([i for i in range(1, grid_row) if i not in exclude_y])
    return [new_y, new_x]

def object_path_algorithm(map, object, obstacle_x, obstacle_y):
    info            = AStarInfo()
    info.GRID_ROW   = len(map.GRID_ROW)  
    info.GRID_COL   = len(map.GRID_COL)  
    info.src        = [object.y, object.x]
    info.dest       = draw_new_target(obstacle_x, obstacle_y, info.GRID_ROW, info.GRID_COL)
    a_star_movement = a_star(info, map.grid)
    del a_star_movement[0] # first element is curent object position
    dirs = make_directions(a_star_movement)
    single_object_path = []
    for index, value in enumerate(dirs):
        world_object_path           = WorldObjectPath()
        world_object_path.map_id    = map.id
        world_object_path.direction = value
        world_object_path.object_id = object.id
        world_object_path.target_y  = info.dest[0]
        world_object_path.target_x  = info.dest[1]
        world_object_path.order     = index
        single_object_path.append(world_object_path)

    return single_object_path

def make_directions(a_star_movement):
    path_dirs = []
    for index, value in enumerate(a_star_movement):
        if(index > 0): 
            if(a_star_movement[index][0] is not a_star_movement[index - 1][0]):
                if(a_star_movement[index][0] < a_star_movement[index - 1][0]):
                    path_dirs.append(Directions.UP)
                elif(a_star_movement[index][0] > a_star_movement[index - 1][0]):
                    path_dirs.append(Directions.DOWN)
            
            elif(a_star_movement[index][1] is not a_star_movement[index - 1][1]):
                if(a_star_movement[index][1] < a_star_movement[index - 1][1]):
                    path_dirs.append(Directions.LEFT)
                elif(a_star_movement[index][1] > a_star_movement[index - 1][0]):
                    path_dirs.append(Directions.RIGHT)


def get_object_path(collide = False):
    for map in get_all_maps():
        static     = get_world_objects(map_id=map.id, static=True)
        idle       = filter(lambda x: x.last_move_monotonic + x.idle_time_tics < time.monotonic(), get_world_objects(static=False, moving=False))
        to_move    = filter(lambda x: x.last_move_monotonic + x.idle_time_tics > time.monotonic(), get_world_objects(static=False, moving=False))
        obstacles  = static + idle
        obstacle_x = list(filter(lambda obj: obj.x, obstacles))
        obstacle_y = list(filter(lambda obj: obj.y, obstacles))

        for object in to_move:
            if(not collide): #can the objects collide?
                obstacle_x.append(object.x)
                obstacle_y.append(object.y)
            yield object_path_algorithm(map, object, obstacle_x, obstacle_y)
            

def create_object_path():
    for world_object_path_list in get_object_path():
        for wrp in world_object_path_list:
            session.add_all(wrp)
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
    return next_moves

def move_objects():
    try:
        for map_id, paths in get_next_moves():
            client_paths = []
            for path in paths:
                world_object = get_world_object(path.object_id)
                if (world_object.next_move_monotic > time.monotonic()):
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
                    
                    client_paths.append(WorldObjectPathClient(world_object.object_id, path.direction, world_object.x, world_object.y, path.target_x, path.target_y))
            
            yield { get_map_by_id(map_id).name: client_paths } #to controller
    except Exception as c:
        print(c) #Todo logs





