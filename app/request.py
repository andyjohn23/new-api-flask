import urllib.request,json
from .models import News_Source, News_Articles


api_key = None
base_url = None
article_url = None


def configure_request(app):
    global api_key, base_url, article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCE_API_BASE_URL']
    article_url = app.config["NEWS_ARTICLES_API_BASE_URL"]


def get_news(category):
    """
    Function that gets the json response to our url request
    """
    get_news_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_sources_url) as url:
        get_sources_data = url.read()
        get_source_response = json.loads(get_sources_data)

        news_source_results = None

        if get_source_response["sources"]:
            news_results_list = get_source_response["sources"]
            news_source_results = process_get_news_sources(news_results_list)

    return news_source_results


def process_get_news_sources(results):
    """
    Function  that processes the news source result and transform them to a list of Objects
    Args:
        news_source_list: A list of dictionaries that contain news source details
    Returns :
        news_source_results: A list of news source objects
    """
    news_source_results = []

    for news in results:
        id = news.get("id")
        name = news.get("name")
        description = news.get("description")
        url = news.get("url")
        category = news.get("category")
        language = news.get("language")
        country = news.get("country")

        if description:
            new_item = News_Source(id,name,description,url,category,language,country)
            news_source_results.append(new_item)

    return news_source_results


def get_news_articles(id):

    get_articles_url = article_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response["articles"]:
            articles_results_list = get_articles_response["articles"]
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles):
    """
    Function  that processes the news article result and transform them to a list of Objects
    Args:
        news_article_list: A list of dictionaries that contain news article details
    Returns :
        news_article_results: A list of news article objects
    """
    news_article_results = []

    for article in articles:
        id = article.get("id")
        title = article.get("title")
        author = article.get("author")
        description = article.get("description")
        url = article.get("url")
        urlToImage = article.get("urlToImage")
        publishedAt = article.get("publishedAt")

        if url:
              article_object = News_Articles(id, title, author, description, url, urlToImage, publishedAt)
              news_article_results.append(article_object)

    return news_article_results
