from flask import Flask, render_template
import json

app = Flask(__name__)
@app.route("/")
def index():
    with open("bernardini_es037_list.json") as f:
        data = json.load(f)
    return render_template("bernardini_es037_route.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, port=1432)