from flask import Flask
from .config import Config
from .db.dev import db
from .db.seeders import seed_commands 
from .routes import channels_bp, teams_bp, docs_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.cli.add_command(seed_commands)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)
app.register_blueprint(teams_bp, url_prefix="/teams")
app.register_blueprint(channels_bp, url_prefix="/channels")
app.register_blueprint(docs_bp, url_prefix="/docs")

@app.route("/")
def index():
        return "<h1>Home</h2>"
    
    
def create_app():
    return app
