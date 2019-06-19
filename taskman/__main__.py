import logging
import configparser
import argparse
import os

from appdirs import user_config_dir, user_data_dir, site_config_dir, site_data_dir

import taskman

CONFIG_FILE_NAME = 'taskman.cfg'
DATA_FILE_NAME = 'taskman.db'
USER_CONFIG_PATH = os.path.join(user_config_dir(taskman.__appname__), CONFIG_FILE_NAME)
SITE_CONFIG_PATH = os.path.join(site_config_dir(taskman.__appname__), CONFIG_FILE_NAME)
USER_DATA_PATH = os.path.join(user_data_dir(taskman.__appname__), DATA_FILE_NAME)


def cmd(subcmd):
    fctn_name = f'cmd_{subcmd}'
    function = globals().get(fctn_name, None)
    if function is None:
        raise Exception(f'Command unknown {subcmd}')

    def wrapper(args):
        if args.verbosity >= 2:
            logging.getLogger().setLevel(logging.DEBUG)
        elif args.verbosity == 1:
            logging.getLogger().setLevel(logging.INFO)
        elif args.quiet:
            logging.getLogger().setLevel(logging.CRITICAL + 1)
            print = str
        else:
            pass
        function(args)

    return wrapper


def cmd_init(args):
    lgr = logging.getLogger('init')
    print('Setup configuration for taskman')

    config = args.config
    if not args.config:
        config = USER_CONFIG_PATH
    config = os.path.abspath(config)
    lgr.info('Path config file: {}'.format(config))

    data = args.data
    if not args.data:
        data = USER_DATA_PATH
    data = os.path.abspath(data)
    lgr.info('Path data file: {}'.format(data))

    cparser = configparser.ConfigParser()
    cparser.add_section('general')
    cparser.set('general', 'data', data)
    cparser.add_section('project_default')
    cparser.set('project_default', 'name', 'Default')

    if os.path.isfile(config):
        print('Configuration file already exists')
        answer = input('Overwrite? (y/N) ')
        if answer or answer == 'y':
            pass
        else:
            print('Canceled!')
            return

    os.makedirs(os.path.dirname(config), exist_ok=True)

    with open(config, 'w') as f:
        cparser.write(f)


def main():
    logging.basicConfig(level=logging.WARNING, style='{', format='{levelname:>8s}: {message}')

    logging.getLogger('base')
    config = configparser.ConfigParser()
    config.read([CONFIG_FILE_NAME, USER_CONFIG_PATH, SITE_CONFIG_PATH])
    print(vars(config))

    argp = argparse.ArgumentParser(description='Manage your tasks')
    argp.add_argument('-c', '--config', help='Path to config file', default=CONFIG_FILE_NAME)

    verbose_xgroup = argp.add_mutually_exclusive_group()
    verbose_xgroup.add_argument('-v', '--verbosity', action='count', default=0)
    verbose_xgroup.add_argument('-q', '--quiet', action='store_true')

    subparsers = argp.add_subparsers()
    parser_init = subparsers.add_parser('init')
    parser_init.set_defaults(func=cmd('init'))
    parser_init.add_argument('--config',
                             help='Create a config file on this path')
    parser_init.add_argument('--data',
                             help='Data will be stored there later on')

    args = argp.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        argp.print_help()


if __name__ == '__main__':
    main()
