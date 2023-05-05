from datetime import datetime
from ..dev import db


class Message(db.Model):
    __tablename__ = "messages"
    # Table Keys
    text = db.Column(db.String(2000))
    sent_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    
    # Foregin Keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    
