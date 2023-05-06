from faker import Faker
from sqlalchemy.sql import text
from app import app
from app.db.dev import db
from app.db.models import User


class UserSeeder:
    def __init__(self):
        self.fake = Faker()

    def generate_users(self, num):
        with app.app_context():
            for _ in range(num):
                user = User(
                    first_name=self.fake.first_name(),
                    last_name=self.fake.last_name(),
                    email=self.fake.email(),
                    hashed_password="password"
                )
                db.session.add(user)
            db.session.commit()

            users = User.query.all()
            return users
        
    @classmethod
    def get_all_users(cls):
        with app.app_context():
            return User.query.all()
        
    @classmethod
    def clear_users(cls):
        with app.app_context():
            deleted_users = db.session.execute(text("DELETE FROM users"))
            num_deleted = deleted_users.rowcount
            db.session.commit()
            return num_deleted


# seeder = UserSeeder()
# seeder.clear_users()
# seeder.generate_users(5)
# users = seeder.get_all_users()
# print(users)
