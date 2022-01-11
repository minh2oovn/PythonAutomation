import logging, os

as53log_path = os.environ['AS53_python']
# AS53_python will be C:\..PycharmProjects\..\AS53pylib\Collectlogs\

def configure_log(level=None, name=None):
    logger = logging.getLogger('Welcome to log world')
    if not len(logger.handlers):
        logger.setLevel(level)
        console_handler = logging.StreamHandler()
        debug_handler = logging.FileHandler(as53log_path + 'as53python.log')
        console_handler.setLevel(logging.DEBUG)
        chFormatter = logging.Formatter('%(asctime)s : %(levelname)s : %(module)s  : %(message)s')
        debug_handler.setFormatter(chFormatter)
        console_handler.setFormatter(chFormatter)
        logger.addHandler(console_handler)
        logger.addHandler(debug_handler)
    return logger

