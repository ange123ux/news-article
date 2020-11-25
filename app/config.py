class Config:
    '''
    General configuration parent class
    '''
    NEW_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}'
    # NEW_API_KEY =os.environ.get('NEW_API_KEY')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True