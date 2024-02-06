import click
from app.cli import cli_bp

@cli_bp.cli.command('create_db')
def create_db():
    print("Running create_db bp")