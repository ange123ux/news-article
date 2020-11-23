class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,description,image,url,publishedAt):
        self.id =id
        self.title = title
        self.description = description
        self.image = 'https://newsapi.org/v2/everything?sources=bbc-news&apiKey=5d18843b84ff4e5d80ba27fbc9b87ca2'+ image
        self.url = url
        self.publishedAt = publishedAt