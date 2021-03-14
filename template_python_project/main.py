import click

@click.command()
@click.option('--first', '-f', required=True, help='First number to handle')
@click.option('--second', '-s', required=True, help='Second number to handle')
def main(first, second):
    print('first: {}, second: {}'.format(first, second))
