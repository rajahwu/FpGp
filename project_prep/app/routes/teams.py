from flask import Blueprint
from ..db.dev import db
from ..db.models import Team

bp = Blueprint("teams", __name__)

@bp.route("/")
def index():
    # all_teams = Team.query.all()
    # print(dict(all_teams))
    return "<h2>Teams Home<h2>"

@bp.route("/all")
def get_teams():
    # all_teams = Team.query.all()
    # print(dict(all_teams))
    return "<h2>All Teams<h2>"

