from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from app.models import user

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
db_migrate = Migrate(app, db)

from app.cli import cli_bp
app.register_blueprint(cli_bp)

from app.core import main