from flask import Flask,render_template
import json

app = Flask(__name__)
@app.route("/")
def home():
    return "<p>Welcome to our Weather Application!</p>"

@app.route("/cities")
def cities():
    return render_template("list.html")
def city():
    @app.route("")
