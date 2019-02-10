# File mode: Read Text file
read_file = open('sample.txt', mode='rt', encoding='utf-8')

# read() allows us to read for a number of characters
first_9 = read_file.read(9)
# Calling read again on the same file returns all the rest of the characters
rest_chars = read_file.read()
# Further reading of the file returns an empty string: ''
after_end_of_file = read_file.read()

# close the file after reading it
# read_file.close()

print("read_file.read(9): ", first_9)
print("read_file.read():", rest_chars)
print("after_end_of_file == '':", after_end_of_file == "")

# seek method puts the marker at any given position of the file, 0 means beginning of the file
read_file.seek(0)

# readline reads a whole line
one_line = read_file.readline()
print("\nread_file.readline()", one_line)

read_file.seek(0)

# readline reads a whole line
whole_file = read_file.readlines()
print("\nread_file.readlines()", whole_file)
