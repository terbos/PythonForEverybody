#7.1 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.

filename = input("Enter a filename: ")
file_handle = open(filename)

for line in file_handle:
    print(line.upper().rstrip())
