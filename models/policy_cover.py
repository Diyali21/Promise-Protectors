import uuid

from extensions import db


class PolicyCover(db.Model):
    __tablename__ = "policy_cover"
    policy_cover_id = db.Column(
        db.String(50), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    policy_id = db.Column(db.String(50))
    cover_id = db.Column(db.Integer)

    def to_dict(self):
        return {
            "policy_cover_id": self.policy_cover_id,
            "policy_id": self.policy_id,
            "cover_id": self.cover_id,
        }
