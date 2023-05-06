from faker import Faker
from sqlalchemy.sql import text
from app import app
from app.db.dev import db
from app.db.models import Team


class TeamSeeder:
    def __init__(self):
        self.fake = Faker()

    def generate_teams(self, num):
        with app.app_context():
            for _ in range(num):
                team = Team(name=self.fake.bs(),
                            image_url=self.fake.image_url())
                db.session.add(team)
            db.session.commit()
            
    @classmethod
    def get_all_teams(cls):
        with app.app_context():
            return Team.query.all()

    @classmethod
    def clear_teams(cls):
        with app.app_context():
            deleted_teams = db.session.execute(text("DELETE FROM teams"))
            num_deleted = deleted_teams.rowcount
            db.session.commit()
            return num_deleted
        
# seeder = TeamSeeder()
# seeder.clear_teams()
# seeder.generate_teams(5)
# teams = seeder.get_all_teams()
# print(teams)
