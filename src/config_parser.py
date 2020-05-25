import json

def parse(fname="config.json"):
    '''Parses the config.json'''
    with open(fname) as f:
        data = json.load(f)
    return data