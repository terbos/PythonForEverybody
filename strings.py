surname = "Papastergiou"
print("String: ",surname)
print("Length: ", len(surname))
print("Taking a part or a letter from a string")
print("First part of String: ",surname[:6])
print("Second part of String: ",surname[6:])
print("Find a count of a letter")

def findLetter(letterToFind):
    count = 0
    for letter in surname:
        if letter == letterToFind:
            count += 1
    print("Letter:",letterToFind,"has appeared", count, "times")

findLetter("a")

print("In Capitals:",surname.upper())
def findIndexOfTheLetter(letter,string):
    index = string.find(letter)
    print("Index of letter",letter,"in string:",string,"is:",index)

findIndexOfTheLetter("g",surname)
findIndexOfTheLetter("ster",surname) #can work with substrings as well

print("Does surnname start with P?",surname.startswith("P"))
print("Does surnname start with p?",surname.startswith("p"))
