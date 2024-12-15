import random

def draw_new_target(ecxlude_x, exclude_y, tiles_x, tiles_y):    
    new_x = random.choice([i for i in range(1,tiles_x) if i not in ecxlude_x])
    new_y = random.choice([i for i in range(1,tiles_y) if i not in exclude_y])
    return {"x" : new_x, "y": new_y }


def generate_path(object, obstacle_x, obstacle_y):
    if (object.x == 0 or object.y == 0):
        return {"error": 0}
    path = None # use path finding algorith (A*) and return directions (direction.py) return array of directions
    # draw_new_target()
    return {} # {object.id: path[moves], "target_x": path["target_x"], "target_y": path["target_y"]}





