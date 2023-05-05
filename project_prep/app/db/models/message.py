from datetime import datetime
from ..dev import db


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())