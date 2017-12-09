filename = input("Enter a filename: ")

try:
    file_handle = open(filename)
except:
    print("There is no such file in the directory.Exiting now")
    quit()

file_handle = open(filename)
for line in file_handle:
    print(line.rstrip()) #use rstrip() to remove new line

file_handle = open(filename)
save_file_to_string = file_handle.read()
print(len(save_file_to_string))
print(save_file_to_string)
print(save_file_to_string[:100])

file_handle = open(filename)
for line in file_handle:
    if line.startswith("But"):
        print("\n",line)
