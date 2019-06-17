import logging
import time
import configparser
import argparse
import os

from appdirs import user_config_dir


def project_add(name: str):
    """
    Save a new project

    :param name: Name of the project
    """
    pass


def project_select(name: str):
    """
    Select the current project

    :param name: Name of the project to select
    """
    pass


def task_add(name: str, priority: int=5, project: str=None, description: str=None):
    """
    Save a new task

    :param name: Name/Title of the task
    :param priority: Priority of the task between 0 and 10
    :param project: Name of the project to add to
    :param description: Description of the task
    """
    pass


def task_show(pk: int):
    pass


def task_summary(project: str=None):
    pass


def main(*args, **kwargs):
    logging.basicConfig(level=logging.WARNING, style='{', format='{asctime}: <{levelname:>8s}> {message}')
    if kwargs.get('verbose', False):
        logging.getLogger().setLevel(logging.DEBUG)

    logger = logging.getLogger('logtest')
    try:
        logger.debug('Running main: debug')
        logger.info('Running main: info')
        logger.warning('Running main: warning')
        logger.error('Running main: error')
        logger.critical('Running main: critical')
        time.sleep(5)
    except KeyboardInterrupt:
        print()
        logger.debug('Stop programm')


if __name__ == '__main__':
    main(verbose=True)
