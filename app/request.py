import urllib.request,json
from .models import News_Source, News_Articles
from config import Config
from datetime import datetime

api_key = Config.NEWS_API_KEY
base_url = Config.NEWS_SOURCE_API_BASE_URL
article_base_url = Config.NEWS_ARTICLES_API_BASE_URL


def configure_request(app):
    global api_key, base_url, article_base_url
    api_key = app.config["NEWS_API_KEY"]
    base_url = app.config["NEWS_SOURCE_API_BASE_URL"]
    article_base_url = app.config["NEWS_ARTICLES_API_BASE_URL"]


def get_news(category):
    """
    Function that gets the json response to our url request
    """
    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_source_results = None

        if get_news_response["sources"]:
            news_results_list = get_news_response["sources"]
            news_source_results = process_news_source(news_results_list)

    return news_source_results

def process_news_source(news_source_list):
    """
    Function  that processes the news source result and transform them to a list of Objects

    Args:
        news_source_list: A list of dictionaries that contain news source details

    Returns :
        news_source_results: A list of news source objects
    """
    news_source_results = []

    for news_item in news_source_list:
        id = news_item.get("id")
        name = news_item.get("name")
        description = news_item.get("description")
        url = news_item.get("url")
        category = news_item.get("category")
        language = news_item.get("language")
        country = news_item.get("country")

        news_object = News_Source(id, name, description, url, category, country, language)
        news_source_results.append(news_object)

        return news_source_results



def get_news_article(id):

    get_articles_url = article_base_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
            articles_results = json.loads(url.read())

            articles_object = None
            if articles_results["news_article"]:
                articles_object = process_news_articles(
                    articles_results["news_article"])

    return articles_object


def process_news_articles(news_article_list):
    """
    Function  that processes the news article result and transform them to a list of Objects

    Args:
        news_article_list: A list of dictionaries that contain news article details

    Returns :
        news_article_results: A list of news article objects
    """
    news_article_results = []
    for news_item in news_article_list:
        id = news_item.get("id")
        title = news_item.get("title")
        author = news_item.get("author")
        description = news_item.get("description")
        url = news_item.get("url")
        urlToImage = news_item.get("urlToImage")
        publishedAt = news_item.get("publishedAt")
        date = news_item.get("date")

        news_object = News_Articles(id,title,author,description,url,urlToImage,publishedAt,date)
        news_article_results.append(news_object)

        return news_article_results

