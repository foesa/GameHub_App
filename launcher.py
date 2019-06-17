class launcher:
    def __init__(self,name,filepath, gamelist):
        self.name = name
        self.filepath = filepath
        self.gamelist = gamelist

    def addGame(self,game):
        self.gamelist.append(game)


    def printGames(self):
        print("Games in "+self.name+":")
        for games in self.gamelist:
            print(games.name+"\n")

    def sortGames(self):
        self.gamelist.sort(key=lambda game: game.name)

