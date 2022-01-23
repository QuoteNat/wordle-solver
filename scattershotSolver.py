class ScattershotSolver:
    def __init__(self, wordList):
        # List of words to work from. Ideally ranked.
        self._wordList = wordList
        # Current guess in the wordList.
        self._counter = 0
        # Columns where the correct letter is known. If the correct letter is unknown
        # the array holds 0.
        self._correctColumns = [0, 0, 0, 0, 0]
        # Incorrect letters for each column. Used for where include letters are not
        self._incorrectColumns = ["", "", "", "", ""]
        # Letters that are in the word.
        self._includedLetters = []
        # Letters that are not in the word.
        self._incorrectLetters = []
        # Guess counter
        self._guessCounter = 0
        # List of guesses to expose letters
        self._guessList = ['AROSE', 'INTEL', 'CUBED', 'PEGGY', 'WHIFF']
    
    def _printDebug(self):
        print("Correct Columns: " + str(self._correctColumns))
        print("Incorrect Columns: " + str(self._incorrectColumns))
        print("Included letters: " + str(self._includedLetters))
        print("Incorrect Letters: " + str(self._incorrectLetters))

    '''Returns the solvers current guess as a string'''
    def getCurrentGuess(self):
        if self._guessCounter < len(self._guessList):
            return self._guessList[self._guessCounter]
        else:
            return self._wordList[self._counter]
    
    def _getNextGuess(self):
        nextGuessFound = False

        # if still exposing letters, do nothing
        if self._guessCounter == len(self._guessList):
            self._printDebug()
            # Iterate through each word in the word list until the next valid guess is found.
            while (not nextGuessFound) and self._counter < (len(self._wordList)-2):
                self._counter += 1
                
                nextGuess = self._wordList[self._counter]
                guessCounter = 0
                notIncorrect = True

                includedLetters = self._includedLetters.copy()

                # check if the word has all the included letters
                for char in nextGuess:
                    if char in includedLetters:
                        includedLetters.remove(char)
                
                if len(includedLetters) != 0:
                    #print(nextGuess + str(includedLetters))
                    notIncorrect = False

                # check every property of the guess that involves iterating each character
                while guessCounter < 5 and notIncorrect:
                    curChar = nextGuess[guessCounter]
                    
                    # reject if an incorrect letter is included in the word
                    if curChar in self._incorrectLetters:
                        notIncorrect = False
                    # reject if the letter does not match up with the correct letter for a column
                    elif self._correctColumns[guessCounter] != 0 and curChar != self._correctColumns[guessCounter]:
                        notIncorrect = False
                    # reject if the letter is known to not be in that specific column (The I response char)
                    elif curChar in self._incorrectColumns[guessCounter]:
                        notIncorrect = False

                    guessCounter += 1
                
                # if all of the above are correct, consider this word to be the next guess
                if notIncorrect:
                    nextGuessFound = True
        
            


    '''Enter the result string of a guess to get the solvers next guess.
    
    param: resultString A string in CIN format, where C is a letter in the correct column,
    I is an included letter, and N is not in the correct word.'''
    def inputResult(self, resultString):
        if self._guessCounter < len(self._guessList):
            curWord = self._guessList[self._guessCounter]
        else:
            curWord = self._wordList[self._counter]
        # iterate through the result string and update member variables to reflect it.
        print(curWord)
        for i in range(len(resultString)):
            match resultString[i]:
                case "C":
                    # update correctColumns to include the correct letter
                    self._correctColumns[i] = curWord[i]
                    # Add the letter to the includeLetters list
                    # NOTE: Not sure if necessary for words with 2 of the same letter.
                    if self._wordList[self._counter][i] not in self._includedLetters:
                        self._includedLetters.append(curWord[i])

                case "I":
                    # Add the letter to the includeLetters list
                    if self._wordList[self._counter][i] not in self._includedLetters:
                        self._includedLetters.append(curWord[i])                    
                    
                    # Add the letter to its respective incorrect column.
                    self._incorrectColumns[i] += curWord[i]
                
                case "N":
                    # Add the letter to the incorrect letters list
                    self._incorrectLetters.append(curWord[i])

        # self._printDebug()
        self._guessCounter += 1
        # Get next guess
        self._getNextGuess()

