file_to_write = input("Enter file - ")

file_handle = open(file_to_write,"w")

line_to_write = "my name is Yiannis\n"

file_handle.write(line_to_write)

file_handle.close()
