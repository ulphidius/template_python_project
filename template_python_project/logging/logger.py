# pylint: disable=too-few-public-methods

import logging
import sys
from datetime import date

class StandardFilter(logging.Filter):
    def filter(self, record):
        allow_levels = [
            logging.DEBUG,
            logging.INFO,
            logging.WARN
        ]

        for allow_level in allow_levels:
            if record.levelno == allow_level:
                return True

        return False

class ErrorFilter(logging.Filter):
    def filter(self, record):
        allow_levels = [
            logging.ERROR,
            logging.CRITICAL
        ]

        for allow_level in allow_levels:
            if record.levelno == allow_level:
                return True

        return False

def init_logger(level, path = None):
    main_module_name = __name__.split('.')[0]
    logger = logging.getLogger(main_module_name)
    handlers = None

    if not path:
        handlers = list()
        handlers.append(logging.StreamHandler(stream=sys.stdout))
        handlers[-1].addFilter(StandardFilter())
        handlers.append(logging.StreamHandler(stream=sys.stderr))
        handlers[-1].addFilter(ErrorFilter())
    else:
        current_date = date.today()
        file_formated_date = current_date.strftime('%Y_%m_%d')
        handlers = logging.FileHandler(
            filename='{path}/{date}_{name}.log'.format(
                path=path,
                date=file_formated_date,
                name=main_module_name
            ),
            mode='a',
            encoding=None,
            delay=False
        )

    formater = logging.Formatter(
        '%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S %p'
    )

    if isinstance(handlers, list):
        for handler in handlers:
            handler.setLevel(level)
            handler.setFormatter(formater)
            logger.addHandler(handler)
    else:
        handlers.setLevel(level)
        handlers.setFormatter(formater)
        logger.addHandler(handlers)

    logger.setLevel(level)
