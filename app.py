from flask import Flask, render_template
from flask_login import LoginManager
from sqlalchemy.sql import text

from config import Config
from extensions import db
from models.user import User
from models.venue import Venue
from routes.about_bp import about_bp
from routes.auth_bp import auth_bp
from routes.confirmation_bp import confirmation_bp
from routes.contact_us_bp import contact_us_bp
from routes.dashboard_bp import dashboard_bp
from routes.faq_bp import faq_bp
from routes.get_cover_bp import get_cover_bp
from routes.history_bp import history_bp
from routes.main_bp import main_bp
from routes.reviews_bp import reviews_bp
from routes.venue_details_bp import venue_details_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the DB
    db.init_app(app)

    with app.app_context():
        try:
            result = db.session.execute(text("SELECT 1")).fetchall()
            print("Connection successful:", result)
        except Exception as e:
            print("Error connecting to the database:", e)

    # Flask - Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(venue_details_bp, url_prefix="/venue-details")
    app.register_blueprint(faq_bp, url_prefix="/faq")
    app.register_blueprint(about_bp, url_prefix="/about")
    app.register_blueprint(contact_us_bp, url_prefix="/contact-us")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(reviews_bp, url_prefix="/reviews")
    app.register_blueprint(get_cover_bp, url_prefix="/get-cover")
    app.register_blueprint(history_bp, url_prefix="/history")
    app.register_blueprint(confirmation_bp, url_prefix="/confirmation")
    app.register_blueprint(auth_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

# Ctrl + ~ -> Open and close terminal
