from flask import Flask,render_template
import json

app = Flask(__name__)
@app.route("/")
def home():
    return "Welcome to our Weather Application!"