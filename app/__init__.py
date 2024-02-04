from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    @app.route('/')
    def main_page():
        return '<h1>Main page</h1>'
    
    return app