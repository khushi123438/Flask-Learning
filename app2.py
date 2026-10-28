from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")

    if name:
        flash(f"Welcome, {name}! Form submitted successfully.", "success")
    else:
        flash("Please enter your name.", "error")

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)


# flashing and redirecting to the same page after form submission.