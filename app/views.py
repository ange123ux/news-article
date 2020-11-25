from flask import render_template
from app import app
# from .request import get_news
from .request import get_news,get_new

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

@app.route('/new/<int:id>')
def new(id):

    '''
    View new page function that returns the new details page and its data
    '''

    new = get_new(id)
    title = f'{new.title}'

    return render_template('new.html',title = title,new = new


  















