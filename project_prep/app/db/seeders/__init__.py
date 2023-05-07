from flask.cli import AppGroup
from .users import UserSeeder
from .teams import TeamSeeder
from .channels import ChannelSeeder
from .messages import MessageSeeder
from .clear_data import clear_all


seed_commands = AppGroup("seed")

users = UserSeeder()
teams = TeamSeeder()
channels = ChannelSeeder()
messages = MessageSeeder()


@seed_commands.command("all")
def seed():
    clear_all()
    users.generate_users(5)
    teams.generate_teams(5)
    channels.generate_channels(5)
    messages.generate_messages(5)

@seed_commands.command("undo")
def undo():
    clear_all()
