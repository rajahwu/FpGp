from flask import Flask
from .config import Config
from .db.dev import db 
from .routes import channels_bp, teams_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)
app.register_blueprint(teams_bp, url_prefix="/teams")
app.register_blueprint(channels_bp, url_prefix="/channels")

@app.route("/")
def index():
    return "<h1>Home</h2>"