from datetime import datetime
from ...dev import db

class team_membership(db.Model):
    __tablename__ = "team_memberships"
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), nullable=False)
    joined_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    
    # Methods
    def __repr__(self):
        return f'<Team (Membership) user_id{self.user_id}, channel_id{self.channel_id}>' 
    