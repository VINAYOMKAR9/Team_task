from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
import sys
from pathlib import Path

# sys.path.append(Path(__file__).resolve().parent.parent)
from fer_app.config import Config
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    # bcrypt.init_app(app)
    # login_manager.init_app(app)
    # login_manager.login_view = 'auth.login'
    #
    # # Blueprints
    # from fer_app.views import auth, trainee, management
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(trainee_bp)
    # app.register_blueprint(management_bp)

    with app.app_context():
        from . import models
        db.create_all()  # Create tables

    return app
