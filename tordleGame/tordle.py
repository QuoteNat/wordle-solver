import random
from enum import Enum

class TordleGame():
    
    class gameState(Enum):
        WON = 1
        LOST = 2
        INCORRECT = 3

    def __init__(self, wordList, word=""):
        # History of guesses
        self._guesses = []
        # Determines if the game is running
        self._gameRunning = True
        if word != "" and len(word) == 5:
            self._word = word
        else:
            self._word = wordList[random.randint(0, len(wordList)-1)].strip()
    
    def __del__(self):
        self._guesses.clear()

    def checkGuess(self, guess):
        responseString = ""
        guess = guess.upper()
        for i in range(5):
            if guess[i] == self._word[i]:
                responseString += "C"
            elif guess[i] in self._word:
                responseString += "I"
            else:
                responseString += "N"
        
        isCorrect = True

        for i in range(5):
            if responseString[i] != "C":
                isCorrect = False
        self._guesses.append(responseString)

        return isCorrect

    def getGuesses(self):
        return self._guesses

    def getCorrect(self):
        return self._word
    
    def isRunning(self):
        return self._gameRunning
    
    """Main gameloop. 
    
    Takes a guess and returns "WON" if the answer is correct. Response key:
    C = letter is in the correct position
    I = letter is not in the correct position but is in the word
    N = letter is not in the word

    Returns a response string if the answer is incorrect.
    Returns an error string if the answer is not valid or the game is complete.
    """
    def runGuess(self, guess):
        guess = guess.upper()

        result = self.checkGuess(guess)
        if result == True:
            self._gameRunning = False
            return self.gameState.WON
        elif result == False and len(self._guesses) == 6:
            self._gameRunning = False
            return self.gameState.LOST
        else:
            return self.gameState.INCORRECT

            
