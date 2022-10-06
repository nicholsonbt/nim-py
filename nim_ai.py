from nim_game import Nim
import random

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

# Gets the name of a player.
def getPlayerName():
    name = input("Enter your name: ")
    
    if name == "AI":
        print("You aren't the AI, I'm the AI!")
        name = getPlayerName()

    return name

# Gets the number of matches to take.
def getMatches():
    return getPosInteger("How many matches do you want to take? ")

# Gets the starting number of matches.
def getStartMatches():
    return getPosInteger("How many matches are in the pile? ")

# Gets the maximum number of matches that can be taken per turn.
def getMatchesPerTurn():
    return getPosInteger("What is the maximum number of matches that can be taken per turn? ")

# Attempts to leave a value of x = n * (k + 1) + 1 for the player, where:
#  k is the maximum number of matches that can be taken per turn.
#  n is an integer greater or equal to 0.
def aiLogic(nim):
    k = nim.maxMatches() + 1
    rem = nim.matchesRemaining() - 1
    
    possibleMoves = [i for i in range(1, k) if (rem - i) % k == 0]
    return possibleMoves[0] if len(possibleMoves) != 0 else random.randrange(1, k)


# Plays the game until someone loses.
def mainloop(nim):
    player = nim.playerTurn()
    
    print("\nIt's " + player + "'s turn. There are " + str(nim.matchesRemaining()) + " matches remaining.")

    if player == "AI":
        matches = aiLogic(nim)

    else:
        matches = getMatches()

    try:
        nim.takeMatches(matches)
        print(player + " took " + str(matches) + " matches.")
    except Exception as e:
        print(e)

    if nim.isGameOver():
        return nim.playerTurn()
    
    return mainloop(nim)

# Plays the game.
def main():
    nim = Nim(getStartMatches(), [getPlayerName(), "AI"], maximum=getMatchesPerTurn())
    print("\n" + mainloop(nim) + " lost.")


if __name__ == "__main__":
    main()
