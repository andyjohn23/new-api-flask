import os


class Config:

    NEWS_SOURCE_API_BASE_URL = "https://newsapi.org/v1/sources?language=en&category={}&apiKey={}"
    NEWS_ARTICLES_API_BASE_URL = "https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}"
    NEWS_API_KEY = os.environ.get("NEWS_API_KEY")


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
