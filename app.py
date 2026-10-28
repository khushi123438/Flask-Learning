from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "home.html",
        name="Khushi",
        course="Artificial Intelligence",
        skills=["Python", "Flask", "Machine Learning"]
    )

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)


## template inheritance and passing data to templates.