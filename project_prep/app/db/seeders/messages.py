from faker import Faker
from sqlalchemy.sql import text
from app import app
from app.db.dev import db
from app.db.models import Message
from .users import UserSeeder

class MessageSeeder:
    def __init__(self):
        self.fake = Faker()
        
    def generate_messages(self, num):
        users = UserSeeder.get_all_users()
        if len(users) == 0:
            UserSeeder.generate_users(5)
        for user in user:
            Message(
                user_id = user.id,
                sent_at = self.fake.datetime()
            )
        
    
    def clear_messages(self):
        with app.app_context():
            deleted_messages = db.session.execute(text("DELETE FROM messages"))
            num_deleted = deleted_messages
            db.session.commit()
            return num_deleted