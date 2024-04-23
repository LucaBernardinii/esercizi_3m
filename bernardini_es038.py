from flask import Flask, render_template
import json

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("bernardini_es038_route.html")

@app.route("/success")
def success():
    return

if __name__ == "__main__":
    app.run(debug=True, port=3412)