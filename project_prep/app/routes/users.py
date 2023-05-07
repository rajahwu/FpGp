from flask import Blueprint
from ..db.models import User


bp = Blueprint("users", __name__)

@bp.route("")
def get_all_user():
    users = User.query.all()
    res = [user.to_dict() for user in users]
    # print(res)
    return {"users":res}