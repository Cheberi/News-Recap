import os

class Config:
    
    NEWS_API_BASE_URL = 'https://newsapi.org/v2'
    NEWS_API_KEY = '126bdc993e31493980198e288c05a967'
    SECRET_KEY = '5300'
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'.format(NEWS_API_KEY)
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}