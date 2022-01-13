import random


class tordleGame():
    # The correct word
    _word = None
    # History of guesses
    _guesses = []
    # Determines if the game is running
    _gameRunning = True

    def __init__(self):
        # create array of words
        words = []
        wordDatabase = open("../database/filtered.txt", "r")
        wordList = wordDatabase.readlines()
        wordDatabase.close()
        self._word = wordList[random.randint(0, len(wordList)-1)].strip()
    
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
            if guess[i] != "C":
                isCorrect == False
        self._guesses.append(responseString)

        return isCorrect

    def getGuesses(self):
        return self._guesses

    def getCorrect(self):
        return self._word
    
    """Main gameloop. 
    
    Takes a guess and returns "Won" if the answer is correct. Response key:
    C = letter is in the correct position
    I = letter is not in the correct position but is in the word
    N = letter is not in the word

    Returns a response string if the answer is incorrect.
    Returns an error string if the answer is not valid or the game is complete.
    """
    # def doGuess(self, guess):
    #     guess = guess.upper()
    #     if len(guess) > 5:
    #         return "Guess must be less than 5 characters"
    #     elif len(self._guesses) == 6:
    #         return "Can't make more than 6 guesses"
    #     else:
            
tordle = tordleGame()
print(tordle.getCorrect())
guess = input()
tordle.checkGuess(guess)
print(tordle.getGuesses())
