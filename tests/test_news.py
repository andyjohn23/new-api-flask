import unittest
from app.models import News_Source, News_Articles

class News_SourceTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the News class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_source = News_Source("CBSN","CBSN NEWS","CBSN is the leading free news platform","cbsn.com","business","us","en")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,News_Source))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,"CBSN")
        self.assertEquals(self.new_source.name,"CBSN NEWS")
        self.assertEquals(self.new_source.description,"CBSN is the leading free news platform")
        self.assertEquals(self.new_source.url,"cbsn.com")
        self.assertEquals(self.new_source.category,"business")
        self.assertEquals(self.new_source.country,"us")
        self.assertEquals(self.new_source.language,"en")

class News_ArticleTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the News article class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.news_article = News_Articles("CBSN","JOHN DOE","Technology Change The World","Technolgy is the best","tech.com","tech.com/tchey.png","20-10-2020")

    def test_instance(self):
        self.assertTrue(isinstance(self.news_article,News_Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.news_article.id,"CBSN")
        self.assertEquals(self.news_article.author,"JOHN DOE")
        self.assertEquals(self.news_article.title,"Technology Change The World")
        self.assertEquals(self.news_article.description,"Technolgy is the best")
        self.assertEquals(self.news_article.url,"tech.com")
        self.assertEquals(self.news_article.urlToImage,"tech.com/tchey.png")
        self.assertEquals(self.news_article.date,"20-10-2020")