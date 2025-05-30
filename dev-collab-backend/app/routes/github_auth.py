from flask import Blueprint, request, jsonify, session, redirect
from app.models import db, User
import os
import requests

github_auth = Blueprint("github_auth", __name__)

CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")


@github_auth.route("/api/auth/github/callback")
def github_callback():
    code = request.args.get("code")
    if not code:
        return jsonify({"error": "Missing code"}), 400

    # Exchange code for access token
    token_response = requests.post(
        "https://github.com/login/oauth/access_token",
        headers={"Accept": "application/json"},
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code,
        },
    )
    token_json = token_response.json()
    access_token = token_json.get("access_token")
    if not access_token:
        return jsonify({"error": "Failed to get access token", **token_json}), 400

    # Fetch user data from GitHub
    user_response = requests.get(
        "https://api.github.com/user",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    user_data = user_response.json()

    if "id" not in user_data or "login" not in user_data:
        return jsonify({"error": "Invalid user data from GitHub", **user_data}), 400

    # Check if user exists or create a new one
    user = User.query.filter_by(github_id=user_data["id"]).first()
    if not user:
        user = User(
            github_id=user_data["id"],
            login=user_data["login"],
            avatar_url=user_data.get("avatar_url"),
        )
        db.session.add(user)
        db.session.commit()

    # Store user ID in session
    session["user_id"] = user.id

    # Redirect to frontend dashboard
    return redirect(f"{FRONTEND_URL}/dashboard")

@github_auth.route("/api/me")
def get_user():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Not logged in"}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "login": user.login,
        "avatar_url": user.avatar_url
    })

@github_auth.route("/api/logout")
def logout():
    session.clear()
    return jsonify({"message": "Logged out"}), 200
