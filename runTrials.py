import solver
import tordleGame.tordle

trials = 0

# print("How many trials would you like to run?")
# trials = int(input())

numGuesses = []
failures = 0

# import wordlist
wordListFile = open("./analysis/columnRating.txt", "r")

wordList = wordListFile.readlines()
trials = len(wordList)
failedWords = []

# filter extraeneous "\n"s
for i in range(len(wordList)):
    wordList[i] = wordList[i].strip()

for i in range(trials):
    game = tordleGame.tordle.TordleGame(wordList, wordList[i])
    solve = solver.Solver(wordList)

    # to solve infinite loop problem
    # backupCounter = 0

    while game.isRunning():
        # get guess
        guess = solve.getCurrentGuess()
        # run guess
        game.runGuess(guess)
        # give response string to solver
        solve.inputResult(game.getGuesses()[len(game.getGuesses())-1])
        # backupCounter += 1
        # print(len(game.getGuesses()))

    
    # enter data
    numGuesses.append(len(game.getGuesses()))
    if game.getGuesses()[len(game.getGuesses())-1] != "CCCCC":
        failedWords.append(wordList[i])
        failures += 1

averageGuesses = 0
for dataPoint in numGuesses:
    averageGuesses += dataPoint

averageGuesses = averageGuesses / trials

print("Attempted to guess " + str(trials) + " words.")
print("Got " + str(trials-failures) + " words correct.")
print("Average guesses: " + str(averageGuesses))
print("Failures: " + str(failures))
print("Failed words: " + str(failedWords))
