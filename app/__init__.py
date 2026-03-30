from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from . import models   

    from .routes import main
    app.register_blueprint(main)

    return app