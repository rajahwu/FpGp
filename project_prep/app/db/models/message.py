from datetime import datetime
from ..dev import db


class Message(db.Model):
    """
    Message model represents a message in the system.

    Attributes:
        id (int): The unique identifier of the message.
        text (str): The content of the message.
        sent_at (datetime): The datetime when the message was sent.
        user_id (int): The ID of the user who sent the message (foreign key).
        channel_id (int): The ID of the channel where the message was sent (foreign key).
        created_at (datetime): The datetime when the message was created.
        updated_at (datetime): The datetime when the message was last updated.

    """
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(2000))
    sent_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f'<Message id: {self.id}, user_id: {self.user_id}, channel_id: {self.channel_id} sent: {self.sent_at}>'
