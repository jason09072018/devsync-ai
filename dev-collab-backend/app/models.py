from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    github_id = db.Column(db.BigInteger, unique=True, nullable=False)
    login = db.Column(db.String, nullable=False)
    avatar_url = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
