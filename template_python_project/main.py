# pylint: disable=too-many-arguments

from logging import DEBUG, INFO, WARNING, ERROR, getLogger
import click
from .core import compute, concat
from .logging import logger

LOGGER = None

@click.group()
@click.option(
    '--log-path',
    '-l',
    default=None,
    help='Path where log files are stored'
)
@click.option('--quiet',
    '-q',
    default=False,
    is_flag=True,
    help='Ignore the information notifications (Conflict with the verbose option)'
)
@click.option(
    '--verbose',
    '-v',
    count=True,
    help="""The first verbose option activate the information notifications
and the second verbose option activate the debug notifications 
(Conflict with the quiet option)"""
)
@click.version_option()
def main(log_path, quiet, verbose):
    global LOGGER

    if quiet and verbose > 0:
        raise click.UsageError(
            'The option quiet and verbose cannot be used together',
            ctx=click.get_current_context()
        )

    if quiet:
        logger.init_logger(ERROR, log_path)
    elif verbose == 1:
        logger.init_logger(INFO, log_path)
    elif verbose == 2:
        logger.init_logger(DEBUG, log_path)
    else:
        logger.init_logger(WARNING, log_path)

    LOGGER = getLogger(__name__.split('.')[0])

    main.add_command(compute_command)
    main.add_command(concat_command)

@main.command(
    name='compute',
    help='Apply a mathematical operation on 2 values'
)
@click.option(
    '--compute-type',
    '-c',
    required=True,
    type=click.Choice(['ADD', 'MUL'], case_sensitive=True)
)
@click.option(
    '--first',
    '-f',
    required=True,
    type=int,
    help='First number to handle'
)
@click.option(
    '--second',
    '-s',
    required=True,
    type=int,
    help='Second number to handle'
)
@click.help_option()
def compute_command(compute_type, first, second):
    if compute_type == 'ADD':
        LOGGER.info('Add function call')
        print(compute.add(int(first), int(second)))

    elif compute_type == 'MUL':
        LOGGER.info('Mul function call')
        print(compute.multiply(int(first), int(second)))

@main.command(
    name='concat',
    help='Command for append 2 strings with a space as separator'
)
@click.option(
    '--first',
    '-f',
    required=True,
    type=str,
    help='First string to handle'
)
@click.option(
    '--second',
    '-s',
    required=True,
    type=str,
    help='Second string to handle'
)
@click.help_option()
def concat_command(first, second):
    print(concat.concat(first, second))
