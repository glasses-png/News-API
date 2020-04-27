from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import Sources

# Views
@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	general = get_articles('top-headlines','category=general')
	sports = get_articles('top-headlines','category=sports')
	technology = get_articles('top-headlines','category=technology')
	entertainment = get_articles('top-headlines','category=entertainment')
	title = "News Chap Chap"

	return render_template('index.html',title = title,general = general, sports= sports,technology=technology,entertainment=entertainment)
	

@main.route('/sources')
@main.route('/sources/<id>')
def articles(id=None):
	'''
	view articles page
	'''
	sources=get_sources()
	from_source = get_articles('top-headlines',f'sources={id}') 
	if id:
		return render_template('sources.html',title='Sources',sources=sources)
		
	else:
		return render_template('sources.html',title='Sources',sources=sources)


