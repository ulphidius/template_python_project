import logging
import sys
from datetime import date

LOGGER = None

def set_logger(level, path):
    global LOGGER

    main_module_name = __name__.split('.')[0]
    logger = logging.getLogger(__name__)
    handler = None

    if not path:
        handler = logging.StreamHandler(stream=sys.stdout)
    else:
        current_date = date.today()
        file_formated_date = current_date.strftime('%Y_%m_%d')
        handler = logging.FileHandler(filename='{path}/{date}_{name}.log'.format(path=path, date=file_formated_date, name=main_module_name), mode='a', encoding=None, delay=False)
    
    handler.setLevel(level)
    formater = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p')
    handler.setFormatter(formater)

    logger.addHandler(handler)
    logger.setLevel(level)

    LOGGER = logger

def get_logger(level, file=None):
    if not LOGGER:
        set_logger(level, file)
    
    return LOGGER
