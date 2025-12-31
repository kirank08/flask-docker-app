import os
from flask import Flask, jsonify

app = Flask(__name__)

PORT = os.getenv("PORT")

if not PORT:
    raise RuntimeError("PORT environment variable is not set")

@app.route("/")
def home():
    return jsonify(
        app_name="Flask Docker App",
        port=PORT
    )

@app.route("/health")
def health():
    return jsonify(status="UP")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(PORT))
