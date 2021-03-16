import click
from .core import compute
from .logging import logger
from logging import INFO

LOGGER = None

@click.command()
@click.option('--compute-type', '-c', type=click.Choice(['ADD', 'MUL'], case_sensitive=True))
@click.option('--first', '-f', required=True, help='First number to handle')
@click.option('--second', '-s', required=True, help='Second number to handle')
@click.option('--log-path', '-l', default=None, help='Path where log files are stored')
@click.version_option()
def main(compute_type, first, second, log_path):
    global LOGGER

    LOGGER = logger.get_logger(INFO, log_path)

    if compute_type == 'ADD':
        LOGGER.info('Add function call')
        print(compute.add(int(first), int(second)))

    elif compute_type == 'MUL':
        LOGGER.info('Mul function call')
        print(compute.multiply(int(first), int(second)))
