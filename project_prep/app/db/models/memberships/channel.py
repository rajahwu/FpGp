from datetime import datetime
from ...dev import db


class ChannelMembership(db.Model):
    """
    Channel Membership model represents the membership of a user in a channel.

    Attributes:
        id (int): The unique identifier of the channel membership.
        type (str): The type of the membership.
        joined_at (datetime): The datetime when the user joined the channel.
        user_id (int): The ID of the user who is a member (foreign key).
        team_id (int): The ID of the team associated with the membership (foreign key).
    """
    __tablename__ = "channel_memberships"
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), nullable=False)
    joined_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("users"), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("users"), nullable=False)
    
    # Methods
    def __repr__(self):
        return f'<Channel (Membership) user_id{self.user_id}, team_id{self.team_id}>' 
    