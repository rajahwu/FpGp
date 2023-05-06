from .users import UserSeeder
from .teams import TeamSeeder
from .channels import ChannelSeeder
from .messages import MessageSeeder

def clear():
    MessageSeeder.clear_messages()
    ChannelSeeder.clear_channels()
    TeamSeeder.clear_teams()
    UserSeeder.clear_users()
    
clear()