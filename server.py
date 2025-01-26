import eventlet
eventlet.monkey_patch(thread=True, time=True)
from cmath import e
from flask import Flask, jsonify, make_response, render_template, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room
from database.model import world_object, map
from database.model.world_object import WorldObject
from database._db import session
from service.db_service import *
from service.world_service import *
from service.util_service import *
from apscheduler.schedulers.background import BackgroundScheduler
import json
import time
from sqlalchemy import text

app = Flask(__name__)
app.config['SECRET_KEY'] = get_setting("secret_key")
app.app_context().push()
socketio = SocketIO(app)
init_db()

### CONTROLLERS ###
@app.route("/", methods=['GET'])
def world():
    config_common = get_config_db("common")
    config_update = next((obj for obj in config_common if obj.key == "default_map_name"), None)
    if config_update:
        config_update.map_name = config_update.default_map_name
    return render_template("world.html", config=json.dumps(config_common))  

# @socketio.on('rootville')
# def rootville():
#     return True

@socketio.on('join_room')
def on_join(data):
    room = data['room']
    join_room(room)
    socketio.emit('message', f'Joined the room: {room}', to=room)

@socketio.on('leave_room')
def on_leave(data):
    room = data['room']
    leave_room(room)    
    print('Leaved room')

# @app.route("/test", methods=['GET'])
# def test():
#     try:
#         objects = session.query(WorldObject).all()
#         return make_response(jsonify([obj.json() for obj in objects]), 200)
#     except Exception as e:
#         return make_response(jsonify({'error message': '{0}'.format(e)}), 500)

### SCHEDULER ###
# @socketio.on('world_objects_update')
# def update_world_objects():
#     try:
#         socketio.emit('world_objects_update', get_all_world_objects_json())
#     except Exception as e:
#         print(e) #TODO: logs

### SCHEDULER FUNC ###
# {"object": object, "paths": path[moves as config.directions], "target_x": true, "target_y": false}
movement = []
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
                    socketio.emit("move_objects", json.dumps({"object_id": mov.id, "dir": dir}), to=map.name)
                    
                    if to_bool(mov["target_x"]) != True and to_bool(mov["target_y"]) != True: #del object info if it reached the target (clear the buffer)
                        del movement[idx_mov]
                        world_object.moving = False
                        world_object.next_move_monotonic = time.monotonic() + world_object.idle_time_monotonic

                    update_world_object(world_object)
    except Exception as c:
        print(e) #Todo logs

def scheduler_start():
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(move_objects, 'interval', seconds=config.move_object_speed_sec, id="move_objects")
    scheduler.start()

socketio.start_background_task(scheduler_start)

if __name__ == '__main__':
    socketio.run(app, debug=True)