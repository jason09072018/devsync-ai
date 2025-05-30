from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SESSION_TYPE"] = "filesystem"
    app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev")
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "None"  # ← important
    app.config["SESSION_COOKIE_SECURE"] = False     # ← only True if running HTTPS

    Session(app)

    db.init_app(app)

    CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

    from app.routes.github_auth import github_auth
    app.register_blueprint(github_auth)

    return app
