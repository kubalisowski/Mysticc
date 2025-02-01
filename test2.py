def move_objects():
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
                    yield {"map_name": map.name, "object_id": mov.id, "dir": dir}
    except Exception as c:
        print(c) #Todo logs