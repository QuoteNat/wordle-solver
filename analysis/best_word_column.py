from column_frequency import getFrequency

def getRating(word):
    rating = 0

    # Add up the ratings of each letter in each column    
    for i in range(5):
        rating += letterFrequency[i][word[i]]

    return rating

letterFrequency = getFrequency()

database = open("../database/filtered.txt", "r")

answerDict = {}

for word in database:
    word = word.strip()
    answerDict[word] = getRating(word)

# https://www.tutorialsteacher.com/articles/sort-dict-by-value-in-python
sortedScores = sorted(answerDict.items(), key=lambda x:x[1], reverse=True)

overallRating = open("./columnRating.txt", "w")
for score in sortedScores:
    overallRating.writelines(score[0] + "\n")
