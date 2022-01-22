# Open the overall wordlist file
wordListFile = open("overallRating.txt", "r")

wordList = wordListFile.readlines()

# filter extraeneous "\n"s
for i in range(len(wordList)):
    wordList[i] = wordList[i].strip()

exposedLetters = []
scattershotWords = []

for word in wordList:
    # how many repeated letters there are
    repeats = 0
    # how many repeated letters can be allowed
    repeatTolerance = 1
    # check if any letter in the word is already accounted for
    for letter in word:
        if letter in exposedLetters and len(scattershotWords) < 5:
            repeats += 1
    
    # if the word exposes five - repeatTolerance new letters, add it
    if repeats <= repeatTolerance and len(scattershotWords) < 5:
        for letter in word:
            if letter not in exposedLetters:
                exposedLetters.append(letter)
        
        scattershotWords.append(word)

# output words
print(len(exposedLetters))
print(scattershotWords)

# Notes:
# Best letter exposure comes with a tolerance of 1 repeat letter per word, allowing for the exposure of 19 letters in five guesses
# 19
# ['AROSE', 'INTEL', 'CUBED', 'PEGGY', 'WHIFF']