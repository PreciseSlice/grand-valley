from flask import render_template
from grand_valley import app

@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html')
def abou():
    return render_template('about.html')

@app.route('/contact.html')
def contac():
    return render_template('contact.html')

@app.route('/recipe-single.html')
def recipe_single():
    return render_template('recipe-single.html')

@app.route('/recipes.html')
def recipes():
    return render_template('recipes.html')

