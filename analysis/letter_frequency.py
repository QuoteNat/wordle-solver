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

# print the percentage of each letter
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Total number of letters is: " + str(totalLetters))

for char in alphabet:
    print(char + ": " + str(letters[char] / totalLetters * 100) + "%")
