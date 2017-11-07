#9.4 Write a program to read through the mbox-short.txt
# and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word
# of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps
# the sender's mail address to a count of the number
# of times they appear in the file.
# After the dictionary is produced, the program
# reads through the dictionary using
# a maximum loop to find the most prolific committer.

#Desired output cwen@iupui.edu 5

filename = open("mbox-short.txt")
dictionary = dict()
for line in filename:
    if line.startswith("From"):
        listed = line.split()
        if listed[0] == "From:":
            continue
        if listed[1] not in dictionary:
            dictionary[listed[1]] = 1
        else:
            dictionary[listed[1]] += 1

value = None
key = None

for i in dictionary:
    if value is None:
        value = dictionary[i]
    elif dictionary[i] > value:
        value = dictionary[i]
        key = i
print(key, value)
