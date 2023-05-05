from datetime import datetime
from ...dev import db


class channel_membership(db.Model):
    __tablename__ = "channel_memberships()"
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), nullable=False)
    joined_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    # Methods
    def __repr__(self):
        return f'<Channel (Membership) user_id{self.user_id}, team_id{self.team_id}>' 
    