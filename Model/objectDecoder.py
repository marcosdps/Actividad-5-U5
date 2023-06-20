import requests
from pathlib import Path
import json

class ObjectDecoder:

    def dataReader(self, movieCtrl):
        response = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=60aa3148d0ba6b2195120778d54f4b20")
        if response.status_code == 200:
            dictionary = response.json()
            self.movieDecoder(dictionary, movieCtrl)
        else: print("Solicitud de datos no procesada")

    def movieDecoder(self, dictionary, movieCtrl):
        for data in dictionary["results"]:
            title = data["original_title"]
            overview = data["overview"]
            originalLang = data["original_language"]
            releaseDate = data["release_date"]
            genres = data["genre_ids"]
            genres = movieCtrl.IDtoGenre(genres)
            movieCtrl.addMovie(title, overview, originalLang, releaseDate, genres)
        #movieCtrl.listarPelis()

    def genreReader(self, movieCtrl):
        with Path("generos.json").open(encoding="UTF-8")as archi:
            genreDictionary=json.load(archi)
            self.genreDecoder(genreDictionary, movieCtrl)
    
    def genreDecoder(self, genreDictionary, movieCtrl):
        for data in genreDictionary["genres"]:
            id = int(data["id"])
            name = data["name"]
            movieCtrl.addGenre(id, name)
        #movieCtrl.listarGeneros()

            


            
            
