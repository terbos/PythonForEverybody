import random

#take the random value
print("\nRandom Values")
for i in range(10):
    x = random.random()
    print(x)

#take the random value in integer from 1-10
print("\nRandom Values from 1-10")
for i in range(10):
    x = int(10 * random.random())
    print(x)

#another way to take random value from 1-10
print("\nGet a random value from a set range")
print(random.randrange(10))

#get a random even number from a range
print("\nGet a random even number from a range")
print(random.randrange(0,101,2))


#save random values from 1-10 to a list
#and make a random choice between them
print("\nMake a random choice from a list")
def randomChoiceFromList(new_range,new_list):
    for i in range(new_range):
        x = int(new_range * random.random())
        new_list.append(x)
    print("The list is: ",new_list)
    print("A Random choice: ", random.choice(new_list))
new_list = list()
randomChoiceFromList(10,new_list)

#suffle a list
def suffleAList(a_list):
    print("\nShuffle a list")
    deck = a_list.split()
    print("The list: ",deck)
    random.shuffle(deck)
    print("The list shuffled: ",deck)

a_list = "ace two three four"
suffleAList(a_list)
