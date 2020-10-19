from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_news, get_news_articles, search_article
from ..models import News_Source, News_Articles


@main.route('/')
def index():
	"""
	view root page function that returns the index the page and its data
	"""
	business_news = get_news("business")
	sports_news = get_news("sports")
	technology_news = get_news("technology")
	entertainment_news = get_news("entertainment")
	health_news = get_news("health")

	search_article = request.args.get("article_query")
		
	if search_article:
		return redirect(url_for('main.search', search_word = search_article))
	return render_template('index.html',health=health_news,business=business_news,sports= sports_news,technology= technology_news,entertainment= entertainment_news)

@main.route("/sources/<id>")
def articles(id):
    """
    the route page for news articles
    """
    article = get_news_articles(id)

    return render_template("article.html", article= article)

