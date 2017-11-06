#8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words
# using the split() method.
#The program should build a list of words.
# For each word on each line check to see
 #if the word is already in the list and if not append it to the list.
 # When the program completes, sort and print the resulting words
 # in alphabetical order.

#desired output
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks',
# 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon',
# 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window',
#'with', 'yonder']

filename = open("romeo.txt")

new_list = list()

for line in filename:
    word_list = line.split()
    for i in range(len(word_list)):
        if word_list[i] not in new_list:
            new_list.append(word_list[i])

print(sorted(new_list))
