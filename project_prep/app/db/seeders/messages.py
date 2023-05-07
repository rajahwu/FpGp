from faker import Faker
from random import choice, randint
from app.db.dev import db
from app.db.models import Message
from app.db.seeders import UserSeeder, ChannelSeeder


class MessageSeeder:
    """
    Seeder class for generating message records.
    """

    def __init__(self):
        self.fake = Faker()

    def generate_messages(self, num=3, users=None, channels=None):
        """
        Generate a random number of messages for all users: range(1, num).

        Args:
            num (int, optional): End range for number of messages. Defaults to 3.
            users (list, optional): List of users to generates messages for. Defaults to None.
            channels (list, optional): List of channels to assigns messages to.

        Returns:
            list: A list of generated message records.
        """

        if not users:
            users = UserSeeder.get_all_users()

        if not channels:
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
        num_deleted = db.session.query(Message).delete()
        db.session.commit()
        return num_deleted
