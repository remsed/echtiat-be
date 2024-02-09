from app import db
from sqlalchemy import SQLAlchemy

class User(db.Model):
    __tablename_ = 'users'

    id = db.Column('user_id', db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Email: {self.email}"