import click
from .core import compute

@click.command()
@click.option('--compute-type', '-c', type=click.Choice(['ADD', 'MUL'], case_sensitive=True))
@click.option('--first', '-f', required=True, help='First number to handle')
@click.option('--second', '-s', required=True, help='Second number to handle')
def main(compute_type, first, second):
    print('compute_type: {}, first: {}, second: {}'.format(compute_type, first, second))
