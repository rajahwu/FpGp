from faker import Faker
from app.db.dev import db
from app.db.models import User


class UserSeeder:
    """
    Seeder class for generating user data.
    """

    def __init__(self):
        """
        Initialize the UserSeeder class.
        """
        self.fake = Faker()

    def generate_users(self, count):
        """
        Generate a specified number of user records.

        Args:
            count (int): The number of user records to generate.

        Returns:
            list : A list of generated user records.
        """
        for _ in range(count):
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
        """
        Querys for all user records.

        Returns:
            list: A list of all user records.
        """
        return User.query.all()

    @classmethod
    def clear_users(cls):
        """
        Deletes all user records.

        Returns:
            int: Number of deleted user records.
        """
        
        num_deleted = db.session.query(User).delete()
        db.session.commit()
        return num_deleted
