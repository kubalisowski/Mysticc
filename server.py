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
from service.navigation_service import *
from service.config_service import *
from apscheduler.schedulers.background import BackgroundScheduler
import json
import time
from sqlalchemy import text
from config import *

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.app_context().push()
socketio = SocketIO(app)
init_db()

### CONTROLLERS ###
@app.route('/', methods=['GET'])
def world():
    client_config = get_client_config()
    client_config['DEFAULT_MAP_NAME'] = setting('DEFAULT_MAP_NAME')
    return render_template('world.html', config=json.dumps(client_config)) 

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

# @app.route('/test', methods=['GET'])
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
# {'object': object, 'paths': path[moves as config.directions], 'target_x': true, 'target_y': false}
movement = []
def emit_move(movement_array):
    for item in move_objects(movement_array):
        socketio.emit('move_objects', json.dumps(item), to=item['map_name'])

def scheduler_start():
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(emit_move, 'interval', args=[movement], seconds=setting('MOVE_OBJECT_FREQUENCY_SEC'), id='move_objects')
    scheduler.start()

socketio.start_background_task(scheduler_start)

if __name__ == '__main__':
    socketio.run(app, debug=True)