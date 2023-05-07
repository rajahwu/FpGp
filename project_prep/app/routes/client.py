from flask import Blueprint, render_template

bp = Blueprint("frontend", __name__, static_folder="static", template_folder="static")

@bp.route("/", defaults={"path": ""})
@bp.route("/<path:path>")
def server_frontend(path):
    return bp.send_static_file('index.html')