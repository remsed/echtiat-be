from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db = SQLAlchemy(app)
    db_migrate = Migrate(app, db)

    from app.cli import cli_bp
    app.register_blueprint(cli_bp)

    from app.models import user

    @app.route('/')
    def main_page():
        return '<h1>Main page</h1>'
    
    return app