from cmath import e
from flask import Flask, jsonify, make_response, render_template
from flask_socketio import SocketIO
from database.model import test, map, game_object
from database.model.test import Test
from database.model.game_object import GameObject
from database._db import session
from service.db_service import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret!"
socketio = SocketIO(app)

init_db()

@app.route("/", methods=['GET'])
def game():
    return render_template("game.html")

@app.route("/test", methods=['GET'])
def test():
    try:
        objects = session.query(GameObject).all()
        return make_response(jsonify([obj.json() for obj in objects]), 200)
    except Exception as e:
        return make_response(jsonify({'error message': '{0}'.format(e)}), 500)

if __name__ == '__main__':
    socketio.run(app, debug=True)