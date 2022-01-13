## TODO: Convert this into a function that returns

def getFrequency():
    # Dictionary of letters and the amount of occurences for each in the database
    letters = {}

    database = open("../database/filtered.txt", "r")

    # total number of letters in every word
    totalLetters = 0

    for word in database:
        # get rid of \n and EOF
        word = word.strip()
        # tally up the amount of letters
        for letter in word:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
            
            totalLetters += 1

    # close datafile
    database.close()

    return letters

# print the percentage of each letter
# print("Total number of letters is: " + str(totalLetters))
# sort the list from highest to lowest
# https://www.tutorialsteacher.com/articles/sort-dict-by-value-in-python
# sortedLetters = sorted(letters.items(), key=lambda x:x[1], reverse=True)

# for item in sortedLetters:
#     print(item[0] + ": {:.2f}%".format(item[1] / totalLetters * 100))

# Total number of letters is: 33780
# E: 10.34%
# S: 9.81%
# A: 9.13%
# R: 6.64%
# O: 6.49%
# I: 5.88%
# L: 5.65%
# T: 5.22%
# N: 5.03%
# D: 3.97%
# U: 3.59%
# C: 3.40%
# Y: 3.00%
# M: 2.98%
# P: 2.95%
# H: 2.81%
# B: 2.55%
# G: 2.40%
# K: 2.02%
# F: 1.73%
# W: 1.59%
# V: 1.17%
# Z: 0.53%
# X: 0.50%
# J: 0.44%
# Q: 0.18%