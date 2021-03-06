"""Custom logger module."""
import logging

from app.config.settings import basepath


class MyFilter(logging.Filter):
    """Custom logger filter."""

    def __init__(self, name='', **kwargs):
        """Initialize MyFilter.

        This filter allows loggers or handlers to log just a specific level.
        kwargs must have levels argument with a list of levels allowed to log.
        """
        self.levels = kwargs.get('levels', [])
        super(MyFilter, self).__init__(name)

    def filter(self, record):
        """Filter record."""
        if record.levelno in self.levels:
            return True
        return False


def get_logger(name='aiohttp_sample', logpath=basepath('logs', 'my.log'),
               info_log=None, error_log=None, loglevel=logging.DEBUG,
               log_format=None, debug=False):
    """Get logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(loglevel)

    fmt = log_format or '%(asctime)s; LEVEL=%(levelname)s; %(message)s'
    formatter = logging.Formatter(fmt)

    if info_log is None and error_log is None:
        file_handler = logging.FileHandler(logpath)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    elif not (info_log and error_log):
        raise ValueError(
            'You must specify info_log and error_log if one of then retrieved')
    else:
        info_handler = logging.FileHandler(info_log)
        info_handler.setLevel(logging.INFO)
        info_handler.setFormatter(formatter)
        info_handler.addFilter(MyFilter(levels=[
            logging.INFO, logging.WARNING]))

        err_handler = logging.FileHandler(error_log)
        err_handler.setLevel(logging.ERROR)
        err_handler.setFormatter(formatter)
        err_handler.addFilter(MyFilter(levels=[
            logging.ERROR, logging.CRITICAL]))
        logger.addHandler(info_handler)
        logger.addHandler(err_handler)

    if debug:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
