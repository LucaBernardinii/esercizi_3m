from flask import Flask, render_template, request 
import json

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("bernardini_es038_route.html")

@app.route("/success", methods=["POST"])
def success():
    username = request.form["Username"]
    return render_template("bernardini_es038_success.html", uname = username)

if __name__ == "__main__":
    app.run(debug=True, port=3412)