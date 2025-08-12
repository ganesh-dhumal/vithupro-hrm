from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello, World! Deployed via Docker + CI/CD on Local for testing 🚀"

if __name__ == "__main__":
    # For local dev only; in Docker we’ll run gunicorn
    app.run(host="0.0.0.0", port=8000)

