import os
from dotenv import load_dotenv

load_dotenv()

__version__ = "0.1.0"

STDOUT_CHANNEL_ID = os.environ.get('STDOUT_CHANNEL_ID')
TEST_GUILD_ID = os.environ.get('TEST_GUILD_ID')
