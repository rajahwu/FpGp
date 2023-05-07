from flask import Blueprint, send_from_directory, current_app

bp = Blueprint("docs", __name__, static_folder="static/docs/html", static_url_path="/docs/html")


@bp.route('/<path:filename>')
def serve_docs(filename):
    return send_from_directory(current_app.static_folder, filename)
