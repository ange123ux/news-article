from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     title = 'Home - Welcome to Online News Articles'
    return render_template('index.html', title = title)

@app.route('/new/<int:new_id>')
def new(new_id):

    '''
    View new page function that returns the new details page and its data
    '''
    return render_template('new.html',id = new_id)















