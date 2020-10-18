from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news
from ..models import News_Source

@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	sources = get_news('general')
	sports_sources = get_news('sports')
	technology_sources = get_news('technology')
	entertainment_sources = get_news('entertainment')

	return render_template('index.html',sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)



