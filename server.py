from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from database._db import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://root:pass@127.0.0.1:3306/world'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

socketio = SocketIO(app)


@app.route("/", methods=['GET'])
def game():
    return render_template("game.html")

if __name__ == '__main__':
    socketio.run(app, debug=True)