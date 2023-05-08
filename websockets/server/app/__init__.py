from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit


app = Flask(__name__)
app.config['SECERT_KEY'] = "Y2/hLtnde+5lOlFC"
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def handle_connect():
    print("WebSocket connected.")
    
@socketio.on("message")
def handle_message(message):
    print("Recieved message: ", message)
    send("Server received your message: " + message, broadcast=True)
    
@socketio.on("disconnect")
def handle_disconnect():
    print("WebSocket disconnected.")
    
if __name__ == '__main__':
    socketio.run(app)

