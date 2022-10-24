import os

from flask import Flask
from .config import Config
from .models import db
from flask_bootstrap import Bootstrap
from app.mysql_service import intert_producto #delete_producto,get_producto


def create_app():
    os.environ.setdefault('FLASK_APP', 'main.py')
    os.environ.setdefault('FLASK_DEBUG', '1')
    os.environ.setdefault('FLASK_ENV', 'development')
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)

    db.init_app(app)


    with app.app_context():
        db.create_all()

    return app