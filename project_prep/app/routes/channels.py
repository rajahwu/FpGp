from flask import Blueprint
from ..db.dev import db
from ..db.models import Channel

bp = Blueprint("channels", __name__)

@bp.route("/")
def index():
    return "<h2>Channels Home<h2>"

@bp.route("/all")
def get_channels():
    # all_channels = Channel.query.all()
    # print(dict(all_channels))
    return "<h2>All Channels<h2>"

