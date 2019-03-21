from app import app
from flask import render_template

title = "Modular Flask"

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('home.html', title=title, user=user)

# @app.route('/about')
# def index():
#     return render_template('about.html', title=title)