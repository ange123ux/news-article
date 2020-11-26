from flask import render_template
from app import app
# from .request import get_news
from .request import get_news,get_new
from .request import get_news,get_new,search_new
from flask import render_template,request,redirect,url_for

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
    
    search_new = request.args.get('new_query')

    if search_new:
        return redirect(url_for('search',new_name=search_new))
    else:
        return render_template('index.html', title = title,business = business_news,entertainment=entertainment_new,sports=sports_new,technology=technology_new)  

@app.route('/new/<int:id>')
def new(id):

    '''
    View new page function that returns the new details page and its data
    '''

    new = get_new(id)
    title = f'{new.title}'

    return render_template('new.html',title = title,new = new)

@app.route('/search/<new_name>')
def search(new_name):
    '''
    View function to display the search results
    '''
    new_name_list = new_name.split(" ")
    new_name_format = "+".join(new_name_list)
    searched_news = search_new(new_name_format)
    title = f'search results for {new_name}'
    return render_template('search.html',news = searched_news)
  















