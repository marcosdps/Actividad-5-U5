

class Genre:
    __id: int
    __name: str

    def __init__(self, id=None, name=None):
        self.__id = id
        self.__name = name

    def showData(self):
        return f"{self.__id} {self.__name}"
    
    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name