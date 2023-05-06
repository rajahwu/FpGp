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
    team_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    
    
    # Methods
    def __repr__(self):
        return f'<Channel id: {self.id}, name: {self.name} team_id: {self.team_id} :: {self.created_at}>'