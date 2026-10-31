
from flask import Flask, render_template, request, flash
import os

from jinja2 import nativetypes

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret"

# Portfolio projects
projects = [
    {
        "title": "Student Management System",
        "description": "A Python application to manage student records, marks and grades.",
        "tech": "Python, SQLite",
        "link": "#"
    },
    {
        "title": "Bank Management System",
        "description": "A banking application with deposit, withdrawal and balance features.",
        "tech": "Python, OOP",
        "link": "#"
    },
    {
        "title": "Personal Portfolio",
        "description": "A responsive personal portfolio website built using Flask.",
        "tech": "Python, HTML, CSS",
        "link": "#"
    }
]


@app.route("/")
def home():
    return render_template("index.html", projects=projects)


@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in all the fields.", "error")
    else:
        # This demo displays a message.
        # It does not send or save the message.
        flash("Thank you! Your message was received.", "success")
    if __name__ == "__main__":
        app.run(debug=True)

    return render_template("index.html", projects=projects)


if __name__ == "__main__":
    app.run(debug=True)
