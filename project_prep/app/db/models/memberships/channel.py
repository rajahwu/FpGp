from datetime import datetime
from ...dev import db


class channel_membership:
    __tablename__ = "channel_memberships"
    id = db.Column(db.Integer, primary_key=True)
    type: db.Column(db.String(150))
    joined_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
    