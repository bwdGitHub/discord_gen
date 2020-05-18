from src.logger import logger
from src.config_parser import parse
from src.client import Gen_Client
from src.transform import GPT2_Transform
import sys

# Set up logger
logger = logger()

# Parse config file
config_file = 'config.json'
if len(sys.argv)>1:
    config_file = sys.argv[1]    
config = parse(config_file)

# optional $github command will point to config['github']
# default just point to my repo.
 
github = config['github'] if 'github' in config else 'https://github.com/bwdGitHub/discord_gen'

# Set up transformer to use
transformer = GPT2_Transform()

# Set up client
client = Gen_Client(transformer,github=github)

# Run
client.run(config['token'])