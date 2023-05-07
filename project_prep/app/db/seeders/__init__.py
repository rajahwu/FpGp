from flask.cli import AppGroup
from .users import *
from .teams import *
from .channels import *
from .messages import *
from .clear_data import clear_all


seed_commands = AppGroup("seed")

users = UserSeeder()
teams = TeamSeeder()
channels = ChannelSeeder()
messages = MessageSeeder()

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'


@seed_commands.command("all")
def seed():
    clear_all()

    num_of = {
        "users": 5,
        "teams": 5,
        "channels": 5,
        # random messages in range(1, messages_per_user)
        "messages_per_user": 5
    }

    user_records = users.generate_users(num_of["users"])
    if len(user_records) >= num_of["users"]:
        raise ValueError(
            RED + "Failed to generate the expected number of user records") + RESET
    else:
        print(
            f'{GREEN}{num_of["users"]} User records successfully generated{RESET} \n {user_records}')

    team_records = teams.generate_teams(num_of["teams"])
    if len(team_records) >= num_of["teams"]:
        raise ValueError(
            RED + "Failed to generate the expected number of user records" + RESET)
    else:
        print(
            f'{GREEN}{num_of["teams"]} Team records successfully generated{RESET} \n {team_records}')

    channel_records = channels.generate_channels(num_of["channels"])
    if len(channel_records) >= num_of["channels"]:
        raise ValueError(
            RED + "Failed to generate the expected number of channel records" + RESET)
    else:
        print(
            f'{GREEN}{num_of["channels"]} Channel Records Generated{RESET} \n {user_records}')

    message_records = messages.generate_messages(
        num_of["messages"], users=user_records, channels=channel_records)
    if len(message_records) < num_of["messages_per_user"]:
        raise ValueError(
            RED + "Failed to generate the expected number of message records" + RESET)
    else:
        print(
            f'{GREEN}{num_of["messages_per_user"]} Messages Records Generated{RESET} \n {message_records}')


@seed_commands.command("undo")
def undo():
    clear_all()
