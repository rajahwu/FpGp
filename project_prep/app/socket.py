from flask_socketio import SocketIO, emit
import os

if os.environ.get("FLASK_ENV") == "production":
    origins = []
else:
    origins = "*"


scoketio = SocketIO(cors_allowed_origins=origins)