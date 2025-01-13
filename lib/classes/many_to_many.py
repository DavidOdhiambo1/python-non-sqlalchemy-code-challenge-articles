class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.all.append(self)
        self.author = author
        self.magazine = magazine
        self.title = title
        

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if (len(title) < 5 or len(title) > 50) or not isinstance(title, str):
            raise TypeError("title must be a string")
        self._title = title  
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author: Firstname Lastname")
        self._author = author
class Author:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name) < 1:
            raise TypeError("name must be a string")
        self._name = name
    
       
    def articles(self):
       
        return [article for article in Article.all if article.author == self]
        

    def magazines(self):
        list_of_magazines = []

        for article in Article.all:
            if article.author == self:
                if article.magazine not in list_of_magazines:
                    list_of_magazines.append(article.magazine)

        return list_of_magazines

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article
            

    def topic_areas(self):
        '''returns a list of topic areas for all articles by author'''
        list_of_categories = []
        for article in Article.all:
            if article.author == self:
                if article.magazine.category not in list_of_categories:
                    list_of_categories.append(article.magazine.category)

        return None if not list_of_categories else list_of_categories
            

        

        
        

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.all.append(self)
        self._articles = []

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise TypeError("name must be a string")
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str) or len(category) < 1:
            raise TypeError("category must be a string")
        self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        list_of_authors = []

        for article in Article.all:
            if article.magazine == self:
                if article.author not in list_of_authors:
                    list_of_authors.append(article.author)

        return list_of_authors
        

    def article_titles(self,):
        return None if not [article.title for article in Article.all if article.magazine == self] else [article.title for article in Article.all if article.magazine == self]
       

    def contributing_authors(self):
        list_of_authors = []

        for article in Article.all:
            if article.magazine == self:
                list_of_authors.append(article.author)
        contributing_authors = {author for author in list_of_authors if list_of_authors.count(author) > 2}    

        return None if not list(contributing_authors) else list(contributing_authors)

    @classmethod
    def top_publisher(cls):
        list_of_magazines = []
        for article in Article.all:
            list_of_magazines.append(article.magazine)

        return None if not list_of_magazines else max(set(list_of_magazines), key = list_of_magazines.count)
            
            

        

        