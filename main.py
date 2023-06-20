from Model.objectDecoder import ObjectDecoder
from Model.manejadorPeli import MovieController
from View.view import visualInterface
from Controller.controller import Controller


if __name__ == "__main__":
    decoder = ObjectDecoder()
    movieCtrl = MovieController()
    genreDictionary = decoder.genreReader(movieCtrl)
    dictionary = decoder.dataReader(movieCtrl)
    ctrl = Controller(movieCtrl)
    myApp = visualInterface(ctrl)
    myApp.run()


