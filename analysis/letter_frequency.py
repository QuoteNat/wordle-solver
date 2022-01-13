# Dictionary of letters and the amount of occurences for each in the database
letters = {}

database = open("../database/filtered.txt", "r")

for word in database:
    # get rid of \n and EOF
    word = word.strip()
    # tally up the amount of letters
    for letter in word:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1

# close datafile
database.close()

print(letters)