from solver import Solver

# import wordlist
wordListFile = open("./analysis/overallRating.txt", "r")

# import wordlist
print("What algorithm would you like to test? 1: Overall rating 2: Column rating")
listInput = input()
wordListFile = open("./analysis/overallRating.txt", "r")

match int(listInput):
    case 1:
        wordListFile.close()
        wordListFile = open("./analysis/overallRating.txt", "r")
    case 2:
        wordListFile.close()
        wordListFile = open("./analysis/columnRating.txt", "r")

wordList = wordListFile.readlines()

# filter extraeneous "\n"s
for i in range(len(wordList)):
    wordList[i] = wordList[i].strip()

solver = Solver(wordList)

responseString = ""

while responseString != "CCCCC":
    print("The solvers current guess is: '" + solver.getCurrentGuess() + "'")
    print("Input the response string (C for correct letter, I for included letter, and N for incorrect letter):")
    responseString = input()

    if responseString != "CCCCC":
        solver.inputResult(responseString)

