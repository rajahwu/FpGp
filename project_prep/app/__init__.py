from flask import Flask
from .config import Config
from .db.dev import db
from .db.seeders import seed_commands 
from .routes import channels_bp, teams_bp, docs_bp, users_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.cli.add_command(seed_commands)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)

app.register_blueprint(teams_bp, url_prefix="/api/teams")
app.register_blueprint(channels_bp, url_prefix="/api/channels")
app.register_blueprint(docs_bp, url_prefix="/api/docs")
app.register_blueprint(users_bp, url_prefix="/api/users")

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def react_root(path):
#     """
#     This route will direct to the public directory in our
#     react builds in the production environment for favicon
#     or index.html requests
#     """
#     if path == 'favicon.ico':
#         return app.send_from_directory('public', 'favicon.ico')
#     return app.send_static_file('index.html')


# @app.errorhandler(404)
# def not_found(e):
#     return app.send_static_file('index.html')

def create_app():
    return app
