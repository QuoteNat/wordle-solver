from solver import Solver

# import wordlist
wordListFile = open("./analysis/overallRating.txt", "r")

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

