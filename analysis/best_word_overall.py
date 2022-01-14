from letter_frequency import getFrequency

def getRating(word):
    rating = 0
    seenList = []
    for letter in word:
        if letter not in seenList:
            rating += letterFrequency[letter]
            seenList.append(letter)
    return rating

letterFrequency = getFrequency()

database = open("../database/filtered.txt", "r")

answerDict = {}

for word in database:
    word = word.strip()
    answerDict[word] = getRating(word)

# https://www.tutorialsteacher.com/articles/sort-dict-by-value-in-python
sortedScores = sorted(answerDict.items(), key=lambda x:x[1], reverse=True)

overallRating = open("./overallRating.txt", "w")
for score in sortedScores:
    overallRating.writelines(score[0] + ": " + str(score[1]) + "\n")
