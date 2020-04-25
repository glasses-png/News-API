from flask import render_template
from app import app
from ..models import Sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources('breaking news')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    title = "News Chap Chap"

    return render_template('index.html', title = title, sources= sources, sports_sources = sports_sources, technology_sources = technology_sources,entertainment_sources = entertainment_sources)
