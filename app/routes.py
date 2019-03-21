from app import app
from flask import render_template

title = "Modular Flask"

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html', title=title)

@app.route('/about')
def index():
    return render_template('about.html', title=title)