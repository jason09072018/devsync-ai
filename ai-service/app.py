# ai-service/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/review", methods=["POST"])
def code_review():
    code = request.json.get("code")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a senior software engineer. Identify bugs, security issues, and suggest optimizations."},
                {"role": "user", "content": f"Code to review:\n\n{code}"}
            ]
        )
        feedback = response.choices[0].message.content
        return jsonify({"feedback": feedback})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)