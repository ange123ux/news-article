import unittest
from models import new
New = new.New

class NewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the New class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_new = New(1234,'Python Must Be Crazy','A thrilling new Python Series','https://newsapi.org/v2/everything?sources=bbc-news&apiKey=5d18843b84ff4e5d80ba27fbc9b87ca2',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_new,New))


if __name__ == '__main__':
    unittest.main()