#5.2 Write a program that repeatedly prompts a user
# for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message
# and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
wrong_input = False
while True:

    user_input = input("Enter integers: ")

    if user_input == "done":
        break

    try:
        user_input = int(user_input)
    except:
        #print("Invalid input!")
        wrong_input = True
        continue

    if smallest is None:
        smallest = user_input
    elif smallest > user_input:
        smallest = user_input
    #print("Current smallest is: ",smallest)
    if largest is None:
        largest = user_input
    elif largest < user_input:
        largest = user_input
    #print("Current largest is: ",largest)

if wrong_input == True:
    print("Invalid input")
print("Maximum is",largest)
print("Minimum is",smallest)
