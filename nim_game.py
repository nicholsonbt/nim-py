class Nim:
    def __init__(self, matches, players, maximum=3):
        if (len(set(players)) != len(players)):
            raise Exception("You can't have repeated player names.")

        if (maximum <= 1):
            raise Exception("The maximum number must be greater than 1.")

        if (len(players) < 2):
            raise Exception("There must be at least two players.")
        
        self.matches = matches
        self.players = players
        self.max = maximum
        self.player = 0
        self.gameOver = False

    # Returns the name of the next player.
    def playerTurn(self):
        return self.players[self.player]

    # Returns whether or not the game is over.
    def takeMatches(self, matches):
        if (self.gameOver):
            raise Exception("The game is already over.")
        
        if (matches < 1 or matches > self.max or matches > self.matches):
            raise Exception("Invalid number of matches taken")

        if (self.matches == matches):
            self.gameOver = True
            self.matches = 0
            return True
            
        else:
            self.matches -= matches
            self.player = (self.player + 1) % len(self.players)
            return False

    # Returns the number of matches remaining.
    def matchesRemaining(self):
        return self.matches

    # Returns the maximum number of matches that can be taken.
    def maxMatches(self):
        return min(self.matchesRemaining(), self.max)

    # Returns whether or not the game is over.
    def isGameOver(self):
        return self.gameOver
