from datetime import datetime
from ..dev import db


class Team(db.Model):
    """
    Team model represents a team in the system.

    Attributes:
        id (int): The unique identifier of the team.
        name (str): The name of the team.
        type (str): The type of the team.
        image_url (str): The URL of the team's image.
        created_at (datetime): The datetime when the team was created.
        updated_at (datetime): The datetime when the team was last updated.
    """
    __tablename__ = "teams"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(150))
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f'<Team id: {self.id}, name: {self.name} :: {self.created_at}>'
