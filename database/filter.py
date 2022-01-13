# Open the unfiltered database
import readline


unfilteredData = open("unfiltered.txt", "r")
# Open the filtered database
filteredData = open("filtered.txt", "w")

# iterate through the unfilteredData, 
# if the word is five letters long (not counting apostrophes), write it to filteredData
for word in unfilteredData:
    # filter the word and make it all caps, since all answers are in all caps in wordle
    word = word.strip().upper()
    if len(word) == 5 and ("'" not in word):
        filteredData.writelines(word + "\n")

# close open files
filteredData.close()
unfilteredData.close()