from nim_game import Nim

# Gets a positive integer (0 not included).
def getPosInteger(question):
    try:
        integer = int(input(question))
        
        if (integer < 0):
            raise ValueError("Negative integer given.")

        else:
            return integer
        
    except ValueError:
        print("Please enter a positive integer (e.g. '2', not 'two').")
        
        return getPosInteger(question)

# Gets the number of players.
def getPlayerCount():
    return getPosInteger("How many players are there? ")

# Gets the name of a player.
def getPlayerName(names, index):
    player_name = input("Enter the name of player " + str(index) + ": ")

    if player_name in names:
        print("There is already a player called " + player_name + ".")
        player_name = getPlayerName(names, index)

    return player_name

# Gets the names of all players.
def getPlayerNames(playerCount):
    player_names = []
    
    for i in range(playerCount):
        player_names.append(getPlayerName(player_names, i + 1))

    return player_names

# Gets the number of matches to take.
def getMatches():
    return getPosInteger("How many matches do you want to take? ")

# Gets the starting number of matches.
def getStartMatches():
    return getPosInteger("How many matches are in the pile? ")

# Gets the maximum number of matches that can be taken per turn.
def getMatchesPerTurn():
    return getPosInteger("What is the maximum number of matches that can be taken per turn? ")

# Plays the game until someone loses.
def mainloop(nim):
    print("\nIt is " + nim.playerTurn() + "'s turn. There are " + str(nim.matchesRemaining()) + " matches remaining.")
    matches = getMatches()

    try:
        nim.takeMatches(matches)
    except Exception as e:
        print(e)

    if nim.isGameOver():
        return nim.playerTurn()
    
    return mainloop(nim)

# Plays the game.
def main():
    nim = Nim(getStartMatches(), getPlayerNames(getPlayerCount()), maximum=getMatchesPerTurn())
    print("\n" + mainloop(nim) + " lost.")


if __name__ == "__main__":
    main()
