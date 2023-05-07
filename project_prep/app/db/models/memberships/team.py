from datetime import datetime
from ...dev import db

class TeamMembership(db.Model):
    """ 
    Team Membership model represents the membership of a user in a team.

    Attributes:
        id (int): The unique identifier of the team membership.
        type (str): The type of the membership.
        joined_at (datetime): The datetime when the user joined the team.
        user_id (int): The ID of the user who is a member (foreign key).
        channel_id (int): The ID of the channel associated with the membership (foreign key).
    """
    __tablename__ = "team_memberships"
    # Common Keys
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), nullable=False)
    joined_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("users"), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("users"), nullable=False)
    
    
    # Methods
    def __repr__(self):
        return f'<Team (Membership) user_id{self.user_id}, channel_id{self.channel_id}>' 
    