from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, template_folder="../client/template", static_folder="../client")
app.config['SECRET_KEY'] = "secret!"
socketio = SocketIO(app)

@app.route("/", methods=['GET'])
def game():
    return render_template("game.html")

if __name__ == '__main__':
    socketio.run(app, debug=True)