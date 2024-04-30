from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/flashcard/<id>")
def flashcards(id):
    with open("bernardini_es039_list.json", "r") as f:
        
    return render_template("bernardini_es039_route.html")
