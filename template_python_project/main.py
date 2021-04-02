import click
from .core import compute
from .logging import logger
from logging import DEBUG, INFO, WARNING, ERROR

LOGGER = None

@click.command()
@click.option('--compute-type', '-c', required=True, type=click.Choice(['ADD', 'MUL'], case_sensitive=True))
@click.option('--first', '-f', required=True, type=int, help='First number to handle')
@click.option('--second', '-s', required=True, type=int, help='Second number to handle')
@click.option('--log-path', '-l', default=None, help='Path where log files are stored')
@click.option('--quiet', '-q', default=False, is_flag=True, help='Ignore the information notifications (Conflict with the verbose option)')
@click.option('--verbose', '-v', count=True, help='The first verbose option activate the information notifications and the second verbose option activate the debug notifications (Conflict with the quiet option)')
@click.version_option()
def main(compute_type, first, second, log_path, quiet, verbose):
    global LOGGER

    if quiet and verbose > 0:
        raise click.UsageError('The option quiet and verbose cannot be used together', ctx=click.get_current_context())

    if quiet:
        LOGGER = logger.get_logger(ERROR, log_path)
    elif verbose == 1:
        LOGGER = logger.get_logger(INFO, log_path)
    elif verbose == 2:
        LOGGER = logger.get_logger(DEBUG, log_path)
    else:
        LOGGER = logger.get_logger(WARNING, log_path)

    if compute_type == 'ADD':
        LOGGER.info('Add function call')
        print(compute.add(int(first), int(second)))

    elif compute_type == 'MUL':
        LOGGER.info('Mul function call')
        print(compute.multiply(int(first), int(second)))
