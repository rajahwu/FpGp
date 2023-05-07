from faker import Faker
from sqlalchemy.sql import text
from random import choice
from app.db.dev import db
from app.db.models import Channel
from . import UserSeeder, TeamSeeder


class ChannelSeeder:
    """
    Seeder class for generating channel data.
    """
    def __init__(self):
        """
        Initialize the ChannelSeeder class.
        """
        self.fake = Faker()

    def generate_channels(self, num=0):
        """
        Generates a specified number of channel records.

        Args:
            num (int, optional): The number of channel records to generate. Defaults to the number of teams.

        Returns:
            list: A list a generated channel records.
        """
        teams = TeamSeeder.get_all_teams()

        if len(teams) == 0:
            TeamSeeder.generate_teams(5)
            teams = TeamSeeder.get_all_teams()

        num_channels = len(teams) if num == 0 else num
        for _ in range(num_channels):
            channel = Channel(
                team_id=choice(teams).id,
                name=self.fake.bs()
            )
            db.session.add(channel)
        db.session.commit()
        channels = Channel.query.all()
        return channels

    @classmethod
    def get_all_channels(cls):
        """
        Querys for all channel records

        Returns:
            list: A list of all channel records.
        """
        return Channel.query.all()

    @classmethod
    def clear_channels(cls):
        """
        Deletes all channel records.

        Returns:
            init: Number of deleted channel records.
        """
        num_deleted = db.session.query(Channel).delete()
        db.session.commit()
        return num_deleted
