import eventlet
eventlet.monkey_patch(thread=True, time=True)
from cmath import e
from flask import Flask, jsonify, make_response, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room
from database.model import map, game_object
from database.model.game_object import GameObject
from database._db import session
from service.db_service import *
from service.game_service import *
from apscheduler.schedulers.background import BackgroundScheduler
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret!"
app.app_context().push()
socketio = SocketIO(app)
init_db()

### CONTROLLERS ###
@app.route("/", methods=['GET'])
def game():
    mapName = 'map1' # later -> dynamic map selection (per user)
    data = {}
    data['map'] = get_map_by_name(mapName).json()
    return render_template("game.html", info=json.dumps(data))  

@socketio.on('joinroom')
def on_join(data):
    room = data['room']
    join_room(room)
    socketio.emit('message', f'Joined the room: {room}', to=room)

@socketio.on('leaveroom')
def on_leave(data):
    room = data['room']
    leave_room(room)    
    print('Leaved room')

# @app.route("/test", methods=['GET'])
# def test():
#     try:
#         objects = session.query(GameObject).all()
#         return make_response(jsonify([obj.json() for obj in objects]), 200)
#     except Exception as e:
#         return make_response(jsonify({'error message': '{0}'.format(e)}), 500)

### SCHEDULER ###
@socketio.on('game_objects_update')
def update_game_objects():
    try:
        #print(get_all_game_objects_json())
        socketio.emit('game_objects_update', get_all_game_objects_json())
    except Exception as e:
        print(e)

def scheduler_start():
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(update_game_objects, 'interval', seconds=1, id="update-game-objects")
    scheduler.start()

socketio.start_background_task(scheduler_start)

if __name__ == '__main__':
    socketio.run(app, debug=True)