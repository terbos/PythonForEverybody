listOfNames = list()

listOfNames = ["Yiannis","Makis","Kostas","Yiorgos","Nikos"]

print("listOfNames:", listOfNames)

listOfYiannis = list()

item_count = 0

for item in listOfNames:
    if item is "Yiannis":
        listOfYiannis.append(listOfNames.pop(item_count))
    item_count += 1

print("listOfNames:", listOfNames)
print("listOfYiannis:", listOfYiannis)
