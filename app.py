from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "🚀 Hello from Flask CI/CD with Jenkins & Docker Quách Kỳ Hiệp! 22DH111096!!!!!!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
