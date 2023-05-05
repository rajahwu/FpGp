from datetime import datetime
from ..dev import db


class Team(db.Model):
    __tablename__ = "teams"
    # Table Keys
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(150))
    image_url = db.Column(db.String(255))
    
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    
    # Methods
    def __repr__(self):
        return f'<Team id: {self.id}, name: {self.name} :: {self.created_at}>'