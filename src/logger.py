import logging

def logger(log_level = logging.DEBUG, log_file = 'gen_discord.log'):
    logger = logging.getLogger('gen_discord')
    logger.setLevel(log_level)
    handler = logging.FileHandler(filename=log_file,encoding='utf-8',mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
    logger.info("Started logger")
    return logger