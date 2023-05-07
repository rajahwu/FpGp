from faker import Faker
from app.db.dev import db
from app.db.models import Team


class TeamSeeder:
    """
    Seeder class for generating team data.
    """
    def __init__(self):
        """
        Initialize the TeamSeeder class.
        """
        self.fake = Faker()

    def generate_teams(self, count):
        """
        Generate a specified number of team records.

        Args:
            count (int): The number of team records to generate.

        Returns:
            list: A list of generated team records.
        """
        for _ in range(count):
            team = Team(name=self.fake.bs(),
                        image_url=self.fake.image_url())
            db.session.add(team)
        db.session.commit()
        teams = Team.query.all()
        return teams

    @classmethod
    def get_all_teams(cls):
        """
        Querys for all team records

        Returns:
            list: A list of all team records.
        """
        return Team.query.all()

    @classmethod
    def clear_teams(cls):
        """
        Deletes all user records.

        Returns:
            int: Number of deleted team records.
        """
        num_deleted = db.session.query(Team).delete()
        db.session.commit()
        return num_deleted

