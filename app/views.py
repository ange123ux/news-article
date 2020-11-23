from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting business news
    business_news = get_news('business')
    entertainment_new = get_news('entertainment')
    sports_new = get_news('sports')
    technology_new = get_news('technology')
    title = 'Home - Welcome to Online News Articles'
    return render_template('index.html', title = title,business = business_news,entertainment=entertainment_new,sports=sports_new,technology=technology_new)  

@app.route('/new/<int:new_id>')
def new(new_id):

    '''
    View new page function that returns the new details page and its data
    '''
    return render_template('new.html',id = new_id)

  















