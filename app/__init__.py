from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from os import environ
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(Config)
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY')

db = SQLAlchemy(app)
db_migrate = Migrate(app, db)
jwt = JWTManager(app)
bcrypt = Bcrypt(app) 

from app.cli import cli_bp
app.register_blueprint(cli_bp)

from app.core import main