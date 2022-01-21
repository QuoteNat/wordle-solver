## TODO: Convert this into a function that returns

def getFrequency():
    # Array of dictionaries of the frequency of each letter in each row
    columns = [{}, {}, {}, {}, {}]
    totalColumnLetters = 0
    database = open("../database/filtered.txt", "r")

    for word in database:
        # get rid of \n and EOF
        word = word.strip()
        # tally up the amount of letters
        for i in range(5):
            letter = word[i]
            if letter not in columns[i]:
                columns[i][letter] = 1
            else:
                columns[i][letter] += 1
        
        totalColumnLetters += 1
            
    # close datafile
    database.close()

    return columns

# TODO: Make good looking display of the data
# print the percentage of each letter
# sort the list from highest to lowest
# https://www.tutorialsteacher.com/articles/sort-dict-by-value-in-python
# results = getFrequency()
# for i in range(5):
#     results[i] = sorted(results[i].items(), key=lambda x:x[1], reverse=True)
#     print(results[i])

# def resultString(i, j):
#     return results[i][0] + ": {:.2f}%".format(results[i][1] / 6756 * 100)

# for i in range(26):
#     print(resultString(0, i) + " " + resultString(1, i) + " " + resultString(2, i) + " " + resultString(3, i) + " " + resultString(4, i) + " ")

# RESULTS
# [('S', 814), ('C', 523), ('B', 504), ('P', 428), ('T', 419), ('M', 387), ('D', 365), ('A', 361), ('L', 332), ('F', 324), ('R', 317), ('G', 308), ('H', 284), ('W', 247), ('E', 188), ('N', 152), ('O', 124), ('V', 124), ('K', 122), ('J', 120), ('I', 103), ('U', 66), ('Y', 53), ('Q', 43), ('Z', 30), ('X', 18)]
# [('A', 1211), ('O', 1014), ('E', 815), ('I', 736), ('U', 591), ('R', 545), ('L', 424), ('H', 294), ('N', 182), ('T', 137), ('P', 112), ('Y', 96), ('C', 95), ('W', 87), ('M', 84), ('D', 62), ('S', 60), ('B', 42), ('V', 36), ('K', 35), ('X', 33), ('G', 24), ('F', 15), ('Z', 12), ('Q', 11), ('J', 3)]
# [('A', 705), ('R', 612), ('I', 610), ('N', 524), ('O', 506), ('L', 477), ('E', 427), ('U', 343), ('T', 320), ('S', 290), ('M', 249), ('D', 220), ('C', 202), ('G', 186), ('P', 172), ('B', 171), ('V', 150), ('K', 105), ('W', 102), ('Y', 92), ('F', 90), ('X', 78), ('Z', 59), ('H', 45), ('J', 16), ('Q', 5)]
# [('E', 1331), ('T', 502), ('N', 471), ('A', 452), ('I', 424), ('L', 403), ('R', 366), ('O', 356), ('S', 283), ('C', 277), ('K', 258), ('D', 255), ('G', 219), ('M', 200), ('P', 193), ('U', 185), ('B', 115), ('F', 111), ('H', 88), ('V', 79), ('W', 75), ('Y', 51), ('Z', 45), ('J', 11), ('X', 4), ('Q', 2)]
# [('S', 1868), ('E', 733), ('Y', 723), ('D', 439), ('R', 403), ('T', 387), ('N', 370), ('A', 355), ('L', 272), ('H', 238), ('O', 191), ('K', 161), ('I', 114), ('P', 90), ('M', 87), ('G', 74), ('C', 52), ('F', 44), ('X', 36), ('Z', 32), ('B', 28), ('W', 27), ('U', 27), ('V', 5)]