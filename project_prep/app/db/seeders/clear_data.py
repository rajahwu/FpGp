from . import TeamSeeder, UserSeeder, MessageSeeder, ChannelSeeder


def clear_all():
    """
    Deletes all records from the users, teams, channels, and messages table.
    """
    MessageSeeder.clear_messages()
    ChannelSeeder.clear_channels()
    TeamSeeder.clear_teams()
    UserSeeder.clear_users()
