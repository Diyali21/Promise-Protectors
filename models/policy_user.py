import uuid

from extensions import db


class PolicyUser(db.Model):
    __tablename__ = "policy_user"
    policy_id = db.Column(
        db.String(50), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    username = db.Column(db.String(25))

    def to_dict(self):
        return {"policy_id": self.policy_id, "username": self.username}
