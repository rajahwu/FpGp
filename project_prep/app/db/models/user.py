from datetime import datetime
from ..dev import db


class User(db.Model):
    """
    User model represents a user in the sytem

   Attributes:
        id (int): The unique identifier of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email address of the user.
        hashed_password (str): The hashed password of the user.
        status (str): The status of the user.
        created_at (datetime): The datetime when the user was created.
        updated_at (datetime): The datetime when the user was last updated.

    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())


    def to_dict(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "status": self.status
        }

    def __repr__(self):
        return f'<User id: {self.id}, email: {self.email} :: {self.created_at}>'
