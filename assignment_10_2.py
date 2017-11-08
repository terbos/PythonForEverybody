#10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day
# for each of the messages.
# You can pull the hour out from the 'From ' line by
# finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

#desired output
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

new_list = list()

dictionary = dict()
filename = open("mbox-short.txt")
for line in filename:
    if line.startswith("From"):
        new_list = line.split()
        if new_list[0] == "From:":
            continue
        if new_list[5] not in dictionary:
            dictionary[new_list[5]] = 1
        else:
            dictionary[new_list[5]] += 1

dictionary2 = dict()

for line in dictionary:
    new_list = line.split(":")
    if new_list[0] not in dictionary2:
        dictionary2[new_list[0]] = 1
    else:
        dictionary2[new_list[0]] += 1

lst = list()
for key,val in dictionary2.items():
    newtup = (key,val) #create a tuple with key and val from dictionary2
    lst.append(newtup) #put tuples in the list

lst = sorted(lst) #sort the list

for key,val in lst[:]:
    print(key,val)
