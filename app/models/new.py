class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://newsapi.org/v2/everything?sources=bbc-news&apiKey=5d18843b84ff4e5d80ba27fbc9b87ca2'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count