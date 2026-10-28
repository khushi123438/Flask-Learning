from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Demo credentials only
DEMO_EMAIL = "test@gmail.com"
DEMO_PASSWORD = "123456"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}

    email = data.get("email", "").strip()
    password = data.get("password", "")

    if email == DEMO_EMAIL and password == DEMO_PASSWORD:
        return jsonify({
            "success": True,
            "message": "Login successful!"
        })

    return jsonify({
        "success": False,
        "message": "Invalid email or password."
    }), 401


if __name__ == "__main__":
    app.run(debug=True)


## APIs with JSON responses:

@app.route("/api/submit", methods=["POST"])
def submit():
    data = request.get_json()

    name = data.get("name")
    subject = data.get("subject")

    return jsonify({
        "message": "Data received successfully",
        "name": name,
        "subject": subject
    })

if __name__ == "__main__":
    app.run(debug=True)

## flask app with API endpoints that return JSON responses.