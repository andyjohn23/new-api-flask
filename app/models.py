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

        
class Articles:
    
    def __init__(self, id,author, title, urlToImage, url):
        self.id = id
        self.author = author
        self.title = title
        self.urlToImage= urlToImage
        self.url = url
        