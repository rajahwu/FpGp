from faker import Faker
from sqlalchemy.sql import text
from random import choice
from app import app
from app.db.dev import db
from app.db.models import Channel
from . import UserSeeder, TeamSeeder


class ChannelSeeder:
    def __init__(self):
        self.fake = Faker()

    def generate_channels(self, num=0):
        with app.app_context():
            teams = TeamSeeder.get_all_teams()

            if len(teams) == 0:
                TeamSeeder.generate_teams(5)
                teams = TeamSeeder.get_all_teams()
            
            num_channels = len(teams) if num == 0 else num
            print(num_channels)
            for _ in range(num_channels):
                channel = Channel(
                    team_id = choice(teams).id,
                    name = self.fake.bs()
                )
                db.session.add(channel)
            db.session.commit()
            
    @classmethod
    def get_all_channels(cls):
        with app.app_context():
            return Channel.query.all()
        
    @classmethod
    def clear_channels(cls):
        with app.app_context():
            deleted_messages = db.session.execute(text("DELETE FROM channels"))
            num_deleted = deleted_messages
            db.session.commit()
            return num_deleted


# seeder = ChannelSeeder()
# ChannelSeeder.clear_channels()
# seeder.generate_channels(15)
# channels = ChannelSeeder.get_all_channels()
# print(channels)
