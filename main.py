from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

now = date.today().year


@app.route("/")
def hello_world():
    return render_template("index.html", year=now)


@app.route("/about")
def about():
    return render_template("about.html", year=now)


@app.route("/contact")
def contact():
    return render_template("contact.html", year=now)


@app.route("/resume")
def resume():
    return render_template("resume.html", year=now)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
