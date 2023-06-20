from Model.classPelicula import Movie
from Model.classGenero import Genre

class MovieController:
    __movieList: list
    __genreList: list

    def __init__(self):
        self.__movieList = []
        self.__genreList = []


    def addMovie(self, title, overview, originalLang, releaseDate, genre_ids):
        aMovie = Movie(title, overview, originalLang, releaseDate, genre_ids)
        self.__movieList.append(aMovie)

    def addGenre(self, id, name):
        aGenre = Genre(id, name)
        self.__genreList.append(aGenre)

    """def listarGeneros(self):
        for i in range(len(self.__genreList)):
            print(self.__genreList[i].showData())"""
    
    """def listarPelis(self):
        for i in range(len(self.__movieList)):
            print(self.__movieList[i].showData())"""
    
    def IDtoGenre(self, genreIDs):
        genreNames = ""
        for id in genreIDs:
            i=0
            while int(id) != self.__genreList[i].getID():
                i +=1
            if i < len(self.__genreList):
                if genreNames != "":
                    genreNames = genreNames + ", "
                genreNames = genreNames + self.__genreList[i].getName()
        return genreNames
    
    def getMovie(self,i):
        return self.__movieList[i]
    
    def getLen(self):
        return len(self.__movieList)


    
    