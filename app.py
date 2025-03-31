venue_details = [
    {
        "venue_id": 1,
        "venue_name": "A secret garden, hidden just for you",
        "venue_description": "Imagine a place, where time stands still, and all that exists is the beauty of nature and the love you share. In this picturesque garden venue, the beauty of nature sets the stage for a romantic and unforgettable wedding celebration. Spend your special day surrounded by the sights, sounds, and scents of nature, your love will flourish, and your hearts will forever be entwined.",
        "max_people": 200,
        "image_link": "https://forbetterforworse.co.uk/wp-content/uploads/2013/07/Manor-by-the-lake-italian-pavilion-ceremony-.jpg",
    },
    {
        "venue_name": "",
        "venue_description": "Envision getting married beneath soaring ceilings and sparkling chandeliers, surrounded by the opulence of a grand banquet hall. This majestic venue transforms into a fairytale setting, where luxurious textures, subtle lighting, and immpecable style converge to create an unforgettable celebration. As you dance beneath the stars, the banquet hall's grandeur and magic will forever be etched in your hearts",
        "max_people": 500,
        "image": "https://media.weddingz.in/images/16ab8276a8bfa26550f679e8e6963687/best-wedding-reception-halls-in-patna-you-will-absolutely-fall-in-love-with.jpg",
    },
    {
        "venue_name": "",
        "venue_description": "Softly glowing sand, whispering waves, and endless blue horizons converge to create an enchanting beachside haven. As the warm breeze carries the sweet scent of saltwater and blooming beach flowers, your love will flourish in this serene coastal setting. With each gentle wave, the beach whispers secrets of forever, as you embark on your new journey together.",
        "max_people": 100,
        "image": "https://img.freepik.com/premium-photo/wedding-arch-with-flowers-beach_640852-4147.jpg",
    },
    {
        "venue_name": "",
        "venue_description": "Within the warm, inviting ambiance of this restaurant venue, the savoury scents of exquisite cuisine, mingle with the sweetness of celebration. Soft lighting dances across rich textures, casting a golden glow on your special day, as the gentle hum of conversation and clinking glasses creates a joyful symphony. As you savor each moment, our restaurant venue transforms into an intimate haven, where love, laughter and delectable delights blend into an unforgettable feast for the senses",
        "max_people": 300,
        "image": "https://weddingvenuemap.com/wp-content/uploads/2018/12/Ceviche-Tapas-Bar-and-Restuarant-Top-Restaurant-Wedding-Venue-A-Magic-Moment-2.jpg",
    },
]

faq = [{"question": "What is wedding insurance", "answer": "wedding insurance"}]


from flask import Flask, render_template

from routes.about_bp import about_bp
from routes.contact_us_bp import contact_us_bp
from routes.dashboard_bp import dashboard_bp
from routes.faq_bp import faq_bp
from routes.main_bp import main_bp
from routes.reviews_bp import reviews_bp
from routes.venue_details_bp import venue_details_bp


def create_app():
    app = Flask(__name__)

    # Flask - Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(venue_details_bp, url_prefix="/venue-details")
    app.register_blueprint(faq_bp, url_prefix="/faq")
    app.register_blueprint(about_bp, url_prefix="/about")
    app.register_blueprint(contact_us_bp, url_prefix="/contact-us")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(reviews_bp, url_prefix="/reviews")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

# Ctrl + ~ -> Open and close terminal
