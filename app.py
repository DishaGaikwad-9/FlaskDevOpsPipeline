
import os

from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/")
def home():
    return jsonify(
        message="Flask DevOps Pipeline API",
        version=APP_VERSION,
        status="running",
    )


@app.route("/health")
def health():
    if os.getenv("SIMULATE_UNHEALTHY") == "true":
        return jsonify(
            status="unhealthy",
            version=APP_VERSION,
        ), 503

    return jsonify(
        status="healthy",
        version=APP_VERSION,
    )


@app.route("/api/message")
def message():
    return jsonify(
        message="Automated build, test, release and rollback!",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
