from datetime import datetime
from ..dev import db


class Channel(db.Model):
    __tablename__ = "channels"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())