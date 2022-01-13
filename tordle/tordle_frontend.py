from tordle import TordleGame

game = TordleGame()
print("Welcome to Tordle!")

while game.isRunning():
    print("Enter a five letter guess:")
    guess = input()
    match game.runGuess(guess):
        case game.gameState.WON:
            print("Correct! You got the correct word in " + str(len(game.getGuesses()))
                + " guesses!")
        case game.gameState.INCORRECT:
            print("Incorrect")
            guesses = game.getGuesses()
            print(guesses[len(guesses)-1])
        case game.gameState.LOST:
            print("Incorrect. You are out of guesses. The word was: " + game.getCorrect())

print("Here are your results!\n")
for guess in game.getGuesses():
    print(guess)