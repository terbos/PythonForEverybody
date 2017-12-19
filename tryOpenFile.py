file_to_open = input("Enter file - ")

try:
    file_handle = open(file_to_open)
    print("File %s exists" % file_to_open)
except:
    print("File %s does not exist" % file_to_open)
