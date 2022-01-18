class Solver:
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
    
    # def __del__(self):
    #     self._wordList.clear()
    #     self._correctColumns.clear()
    #     self._incorrectColumns.clear()
    #     self._includedLetters.clear()
    #     self._incorrectLetters.clear()
    #     self._counter = 0
    def _printDebug(self):
        print("Correct Columns: " + str(self._correctColumns))
        print("Incorrect Columns: " + str(self._incorrectColumns))
        print("Included letters: " + str(self._includedLetters))
        print("Incorrect Letters: " + str(self._incorrectLetters))

    '''Returns the solvers current guess as a string'''
    def getCurrentGuess(self):
        return self._wordList[self._counter]
    
    def _getNextGuess(self):
        nextGuessFound = False

        # Iterate through each word in the word list until the next valid guess is found.
        while (not nextGuessFound) and self._counter < (len(self._wordList)-2):
            self._counter += 1
            
            nextGuess = self._wordList[self._counter]
            guessCounter = 0
            notIncorrect = True

            includedLetters = self._includedLetters

            # check if the word has all the included letters
            for char in nextGuess:
                if char in includedLetters:
                    includedLetters.remove(char)
            
            if len(includedLetters) != 0:
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
        # iterate through the result string and update member variables to reflect it.
        for i in range(len(resultString)):
            match resultString[i]:
                case "C":
                    # update correctColumns to include the correct letter
                    self._correctColumns[i] = self._wordList[self._counter][i]
                    # Add the letter to the includeLetters list
                    # NOTE: Not sure if necessary for words with 2 of the same letter.
                    self._includedLetters.append(self._wordList[self._counter][i])

                case "I":
                    # Add the letter to the includeLetters list
                    self._includedLetters.append(self._wordList[self._counter][i])
                    # Add the letter to its respective incorrect column.
                    self._incorrectColumns[i] += self._wordList[self._counter][i]
                
                case "N":
                    # Add the letter to the incorrect letters list
                    self._incorrectLetters.append(self._wordList[self._counter][i])

        # self._printDebug()
        
        # Get next guess
        self._getNextGuess()

