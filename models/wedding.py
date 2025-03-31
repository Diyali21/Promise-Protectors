import uuid

from extensions import db


class Wedding(db.Model):
    __tablename__ = "wedding"
    wed_id = db.Column(db.Integer, primary_key=True, default=lambda: str(uuid.uuid4()))
    no_guests = db.Column(db.Integer, nullable=False)
    wed_date = db.Column(db.DateTime, nullable=False)
    venue_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(25), nullable=False)
    package_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "wed_id": self.wed_id,
            "no_guests": self.no_guests,
            "wed_date": self.wed_date,
            "venue_name": self.venue_name,
            "username": self.username,
            "package_id": self.package_id,
        }
