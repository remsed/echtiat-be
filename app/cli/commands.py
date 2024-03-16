import click
from app.cli import cli_bp
from app import db
from app.models.user import User

@cli_bp.cli.command('create_db')
def create_db():
    db.create_all()
    print('Create database: Done.')

@cli_bp.cli.command('drop_db')
def drop_db():
    db.drop_all()
    print('Drop database: Done.')

@cli_bp.cli.command('populate_db')
def populate_db():
    test_user = User(fname='fname01',
                     lname='lname01',
                     email='fname01.lname01@example.com',
                     password='fname01.lname01')
    db.session.add(test_user)
    db.session.commit()
    print('Populate database: Done.')