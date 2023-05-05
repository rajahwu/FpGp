from datetime import datetime
from ...dev import db


class team_membership(db.Model):
    __tablename__ = "team_memberships"
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    type: db.Column(db.String(150))
    joined_at = db.Column(db.DateTime, nullable=False, defalut=datetime.now())
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    