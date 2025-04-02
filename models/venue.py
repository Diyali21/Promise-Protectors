import uuid

from extensions import db


class Venue(db.Model):
    __tablename__ = "venue"
    venue_id = db.Column(
        db.Integer, primary_key=True, default=lambda: str(uuid.uuid4())
    )
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)
    venue_image = db.Column(db.String(255), nullable=False)
    venue_price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "venue_id": self.venue_id,
            "name": self.name,
            "description": self.description,
            "max_guests": self.max_guests,
            "venue_image": self.venue_image,
            "venue_price": self.venue_price,
        }
