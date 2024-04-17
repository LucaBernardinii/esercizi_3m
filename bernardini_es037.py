from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    return "bernardini_es037_list"


@app.route("/text/")
def testo():
    with open("bernardini_es037_list.json") as f:
        data = json.load(f)
    return data

@app.route("/href/")
def link():
    with open("bernardini_es037_list.json") as f:
        data = json.load(f)




if __name__ == "__main__":
    app.run(debug=True, port=1234)