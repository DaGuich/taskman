import logging
import configparser
import os.path

from appdirs import user_config_dir, user_data_dir, site_config_dir, site_data_dir

import taskman

CONFIG_FILE_NAME = 'taskman.cfg'
USER_CONFIG_PATH = os.path.join(user_config_dir(taskman.__appname__), CONFIG_FILE_NAME)
SITE_CONFIG_PATH = os.path.join(site_config_dir(taskman.__appname__), CONFIG_FILE_NAME)


def main(*args, **kwargs):
    logging.basicConfig(level=logging.WARNING, style='{', format='{levelname:>8s}: {message}')
    if kwargs.get('verbose', False):
        logging.getLogger().setLevel(logging.DEBUG)
    try:
        logging.getLogger('base')
        config = configparser.ConfigParser()
        config.read([CONFIG_FILE_NAME, USER_CONFIG_PATH, SITE_CONFIG_PATH])
    except KeyboardInterrupt:
        print()
        logging.getLogger('exit').info('Exit taskman early')


if __name__ == '__main__':
    main(verbose=True)
