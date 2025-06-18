
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from fer_app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Import and register blueprints
    from fer_app.views.auth import auth_bp
    from fer_app.views.trainee import trainee_bp
    # from fer_app.views.management import management_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(trainee_bp)
    # app.register_blueprint(management_bp)

    # Create tables
    with app.app_context():
        try:
            from fer_app import models  # Ensure models are imported
            db.create_all()
            print("✅ Database connected successfully")
        except Exception as e:
            print("❌ Database connection failed:", str(e))

    return app
