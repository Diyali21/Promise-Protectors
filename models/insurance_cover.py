from extensions import db


class InsureCover(db.Model):
    __tablename__ = "insurance_cover"
    cover_id = db.Column(db.Integer, primary_key=True)
    cover_name = db.Column(db.String(50), nullable=False)
    cover_price = db.Column(db.Float, nullable=False)
    cover_description = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            "cover_id": self.cover_id,
            "cover_name": self.cover_name,
            "cover_price": self.cover_price,
        }
