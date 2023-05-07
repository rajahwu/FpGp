from . import TeamSeeder, UserSeeder, MessageSeeder, ChannelSeeder


def clear_all():
    MessageSeeder.clear_messages()
    ChannelSeeder.clear_channels()
    TeamSeeder.clear_teams()
    UserSeeder.clear_users()
