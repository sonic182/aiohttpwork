"""Main script."""
from os import environ

import argparse
import uvloop
from aiohttp import web

from app.config.settings import basepath
from app.config.logger import get_logger
from app.config.application import app_config
from app.middlewares import MIDDLEWARES

uvloop.install()


def parse_args():
    """Parse cli args."""
    parser = argparse.ArgumentParser(description='Run application.')

    parser.add_argument(
        'port',
        type=int,
        default=8080,
        nargs='*',
        help='application port.'
    )

    parser.add_argument(
        '--debug',
        action='store_true',
    )

    return parser.parse_args()


def main():
    """Start app."""
    args = parse_args()
    logger = get_logger(
        debug=args.debug,
        info_log=basepath('logs', 'info.log'),
        error_log=basepath('logs', 'error.log'),
    )

    app = web.Application(
        debug=args.debug,
        logger=logger,
        middlewares=MIDDLEWARES
    )
    app_config(app)
    app.logger.info('MODE=%s; Starting app on port %i' % (environ.get(
        'APP_ENV', 'develop'), args.port))

    web.run_app(
        app,
        port=args.port,
        access_log=None
    )


if __name__ == '__main__':
    main()
