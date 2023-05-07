from datetime import datetime
from ..dev import db


class Channel(db.Model):
    """ 
    Channel model represents a channel in the system.

    Attributes:
        id (int): The unique identifier of the channel.
        name (str): The name of the channel.
        description (str): The description of the channel.
        type (str): The type of the channel.
        image_url (str): The URL of the channel's image.
        team_id (int): The ID of the team to which the channel belongs (foreign key).
        created_at (datetime): The datetime when the channel was created.
        updated_at (datetime): The datetime when the channel was last updated.
    """
    __tablename__ = "channels"
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(2000))
    type = db.Column(db.String(150))
    image_url = db.Column(db.String(255))
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    
    def __repr__(self):
        return f'<Channel id: {self.id}, name: {self.name} team_id: {self.team_id} :: {self.created_at}>'