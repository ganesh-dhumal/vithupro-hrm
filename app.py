from flask import Flask

app = Flask(__name__)

@app.get("/")
def root():
    return "Hello, World! Deployed via Jenkins + Docker 🧩"

if __name__ == "__main__":
    # Dev only; in Docker we use gunicorn (see Dockerfile)
    app.run(host="0.0.0.0", port=8000, debug=False)
