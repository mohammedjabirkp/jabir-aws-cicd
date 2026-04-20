from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello Jabir, CI/CD is working!</h1>"

@app.route("/status")
def status():
    return "<h3>Server is running successfully on AWS EC2</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
