from src.logger import logger
from src.config_parser import parse
from src.client import Gen_Client
import sys

# Set up logger
logger = logger()

# Parse config file
config_file = 'config.json'
if len(sys.argv)>1:
    config_file = sys.argv[1]    
config = parse(config_file)

# Set up client
client = Gen_Client()

# Run
client.run(config['token'])