import urllib.request,json
from .models import News_Sources, News_Articles

apiKey = None
base_url = None
news_article_url = None

def configure_request(app):
    global apiKey, base_url,news_article_url
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCE_API_BASE_URL']
    news_article_url = app.config['NEWS_ARTICLE_API_BASE_URL']

def get_news(category):
    """
    Function that gets the json response to our url request
    """
    get_news_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_news_sources(news_results_list)
    return news_results

def process_news_sources(news_list):
    """
    Function  that processes the news source result and transform them to a list of Objects
    Args:
        news_source_list: A list of dictionaries that contain news source details
    Returns :
        news_source_results: A list of news source objects
    """

    news_results=[]

    for news_item in news_list:
        id = news_item.get('id')
        name= news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')

        news_object= News_Sources(id,name,description, url, category, country)
        news_results.append(news_object)
    
    return news_results

def get_articles(id):
    '''
    Function that gets the json response to the url request
    '''
    get_articles_url = news_article_url.format(id,apiKey)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        news_articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            news_articles_results = process_articles(articles_results_list)
    return news_articles_results

def process_articles(article_list):
    """
    Function  that processes the news article result and transform them to a list of Objects
    Args:
        news_article_list: A list of dictionaries that contain news article details
    Returns :
        news_article_results: A list of news article objects
    """
    news_articles_results = []

    for article_item in article_list:
        title = article_item.get('title')
        author = article_item.get('author')
        description = article_item.get('description')
        url= article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        articles_object = News_Articles(title,author,description, url, urlToImage, publishedAt)
        news_articles_results.append(articles_object)
    return news_articles_results