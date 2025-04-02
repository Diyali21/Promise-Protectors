from flask_login import UserMixin

from extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    username = db.Column(db.String(25), primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    contact_no = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            "username": self.username,
            "fullname": self.fullname,
            "email": self.email,
            "contact_no": self.contact_no,
            "password": self.password,
        }

    def get_id(self):
        return self.username
