
class Controller:
    __movieController = object

    def __init__(self, movieController):
        self.__movieController = movieController

    def getListLen(self):
        return self.__movieController.getLen()
    
    def getTitle(self,i):
        aMovie = self.__movieController.getMovie(i)
        return aMovie.getTitle()
    
    def getLenguage(self, index):
        aMovie = self.__movieController.getMovie(index)
        return aMovie.getOriginalLanguage()
    
    def getOverV(self, index):
        aMovie = self.__movieController.getMovie(index)
        return aMovie.getOverview()
    
    def getRDate(self, index):
        aMovie = self.__movieController.getMovie(index)
        return aMovie.getReleaseDate()
    
    def getGen(self, index):
        aMovie = self.__movieController.getMovie(index)
        return aMovie.getGenre()
    
    
