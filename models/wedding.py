import uuid

from extensions import db


class Wedding(db.Model):
    __tablename__ = "wedding"
    wed_id = db.Column(
        db.String(50), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    no_guests = db.Column(db.Integer, nullable=False)
    wed_date = db.Column(db.DateTime, nullable=False)
    venue_id = db.Column(db.Integer)
    total_price = db.Column(db.Float)
    username = db.Column(db.String(25))

    def to_dict(self):
        return {
            "wed_id": self.wed_id,
            "no_guests": self.no_guests,
            "wed_date": self.wed_date,
            "venue_name": self.venue_id,
            "total_price": self.total_price,
            "username": self.username,
        }
