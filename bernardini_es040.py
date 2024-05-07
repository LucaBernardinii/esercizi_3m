from flask import Flask, render_template
import json

app = Flask(__name__)

def get_recipe_by_id(id: int) -> None:
    with open("bernardini_es040_list.json", "r") as f:
        recipes = json.load(f)
    for recipe in recipes:
        if recipe["id"] == id:
            print(recipe)
            return recipe

@app.route("/recipe/<int:id>")
def recipe(id):
    recipe = get_recipe_by_id(id)
    return render_template("bernardini_es040_route.html", recipe=recipe)

@app.route("/recipes")
def get_all_recipes():
    return render_template("bernardini_es040_recipes.html")

if __name__ == "__main__":
    app.run(debug=True, port=3412)