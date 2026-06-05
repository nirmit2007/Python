class Movie:

    def __init__(self,name,genre):
        print("Default Constructor Of Movie is Called")
        self.name = name  
        self.genre = genre

class Type(Movie):

    def __init__(self,name,genre):
        super().__init__(name,genre)
        print("Type Class Constructor Called")

    def getMovieInfo(self):
        print("Name : ",self.name)
        print("Genre : ",self.genre)

m = Type("John Wick","Action")
m.getMovieInfo()