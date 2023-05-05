from datetime import datetime
from ..dev import db


class Channel(db.Model):
    __tablename__ = "channels"
    # Table Keys
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(2000))
    type = db.Column(db.String(150))
    image_url = db.Column(db.String(255))
    
    # Foreign Keys
    team_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())