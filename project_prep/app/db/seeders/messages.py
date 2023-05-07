from faker import Faker
from sqlalchemy.sql import text
from random import choice, randint
from app.db.dev import db
from app.db.models import Message
from . import UserSeeder, ChannelSeeder


class MessageSeeder:
    """
    Seeder class for generating message records.
    """
    def __init__(self):
        self.fake = Faker()

    def generate_messages(self, num=3):
        """
        Generate a random number of messages for all users: range(1, num).

        Args:
            num (int, optional): End range for number of messages. Defaults to 3.

        Returns:
            list: A list of generated message records.
        """
        users = UserSeeder.get_all_users()
        channels = ChannelSeeder.get_all_channels()

        if len(users) == 0:
            UserSeeder.generate_users(5)
            users = UserSeeder.get_all_users()

        if len(channels) == 0:
            ChannelSeeder.generate_channels(5)
            channels = ChannelSeeder.get_all_channels()

        for user in users:
            for _ in range(randint(1, num)):
                message = Message(
                    user_id=user.id,
                    channel_id=choice(channels).id,
                    text=self.fake.sentence(),
                    sent_at=self.fake.date_time()
                )
                db.session.add(message)
        db.session.commit()
        messages = Message.query.all()
        return messages

    @classmethod
    def clear_messages(cls):
        """
        Deletes all message records.

        Returns:
            int: Number of deleted message records.
        """
        deleted_messages = db.session.execute(text("DELETE FROM messages"))
        num_deleted = deleted_messages
        db.session.commit()
        return num_deleted
