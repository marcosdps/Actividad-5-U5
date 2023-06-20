

class Movie:
    __title: str
    __overview: str
    __originalLang: str
    __releaseDate: str
    __genre: str

    def __init__(self, title=None, overview=None, originalLang=None, releaseDate=None, genres=None):
        self.__title = title
        self.__overview = overview
        self.__originalLang = originalLang
        self.__releaseDate = releaseDate
        self.__genre = genres

    def showData(self):
        return f"Title: {self.__title}\n Original Language: {self.__originalLang}\n Release Date: {self.__releaseDate}\n Genre: {self.__genre}\n Overview: {self.__overview} \n "
        
    def getTitle(self):
        return self.__title
    
    def getOverview(self):
        return self.__overview
    
    def getOriginalLanguage(self):
        return self.__originalLang
    
    def getReleaseDate(self):
        return self.__releaseDate
    
    def getGenre(self):
        return self.__genre