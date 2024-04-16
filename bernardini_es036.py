from flask import Flask, render_template
import json

app = Flask(__name__)

def carica_file():
    with open("bernardini_es036_list", "r") as file_json:
        bernardini_es036_list = json.load(file_json)
    return bernardini_es036_list

@app.route("/")
def index():
    return "bernardini_es036_list"

@app.route("/Student")
def student():
    return render_template("bernardini_es036_route.html")

@app.route("/Vote")
def vote():
    return render_template("bernardini_es036_route.html")