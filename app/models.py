class News_Source:
    """
    News-source class to define News Objects
    """
    source_list = []

    
    def __init__(self,id,name,description,url,category,language,country):
        """
        Initiliazing the variables of the class
        """
        self.id = id 
        self.name = name 
        self.description = description
        self.url = url 
        self.category = category 
        self.language = language
        self.country = country 

        
class News_Articles:
    """
    News articles class to define news-article objects
    """

    def __init__(self,id,title,author,description,url,urlToImage,publishedAt,date):
        """
        Initiliazing the variables of the class
        """
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.date = date
        