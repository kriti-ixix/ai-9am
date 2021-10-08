from random import choice

correctGuess = []
wrongGuess = []

def checkGuess(guess):
    if guess in movieChosen:
        correctGuess.append(guess)
        print("Your guess was correct")
    else:
        wrongGuess.append(guess)
        print("Your guess was incorrect")

def printMovie():
    for i in movieChosen:
        if i==' ':
            print(" ", end="")
        elif i in correctGuess:
            print(i, end=" ")
        else:
            print("_ ", end="")

listOfMovies = ["shang chi", "shershah", "3 idiots", "tiger zinda hai", "dangal"]
movieChosen = choice(listOfMovies)
turns = 10
#print(movieChosen)

while turns > 0:
    printMovie()
    print("\nNumber of turns left:", turns)
    userGuess = input("Enter your guess: ")
    checkGuess(userGuess)
    turns -= 1
else:
    print("Game over! You lost :/")