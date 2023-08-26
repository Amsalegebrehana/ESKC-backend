from flask import Flask
# from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config') # Load configuration from 'config' module
    
    db.init_app(app)
    migrate.init_app(app, db) 

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app

# app = create_app()
