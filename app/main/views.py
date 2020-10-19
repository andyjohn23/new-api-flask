from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news, get_articles
from ..models import News_Source, Articles

@main.route('/')
def index():
	"""
	view root page function that returns the index the page and its data
	"""
	business_news = get_news("business")
	sports_news= get_news("sports")
	technology_news= get_news("technology")
	entertainment_news= get_news("entertainment")
	health_news=get_news("health")

	return render_template('index.html',health=health_news,business=business_news,sports= sports_news,technology= technology_news,entertainment= entertainment_news)

@main.route('/sources/<id>')
def articles(id):
    '''
    route page for articles and the content availabe
    '''
    article = get_articles(id)

    return render_template('article.html', article= article)