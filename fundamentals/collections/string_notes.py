# strings are homogeneous immutable sequence of unicode chars

# the common usage with the other languages:
print("len('English'):", len('English'))
# Strings are immutable so += re-binds variables reference to a new var. This may cause performance degradation
print("'Eng' + 'lish':", 'Eng' + 'lish')
print("names = ', '.join(['John', 'Bill', 'Anna']):", ', '.join(['John', 'Bill', 'Anna']))
names = ', '.join(['John', 'Bill', 'Anna'])
print("names.split(','): ", names.split(","))
# python idiomatic string concatenation:
print("''.join(['concatenated', ' ', 'string']):", ''.join(['concatenated', ' ', 'string']))

# use partition() together with tuple unpacking to destruct string into sub-strings
departure, separator, destination = "Montreal->Toronto".partition('->')
print("\ndeparture, separator, destination:", departure, separator, destination)
# _ usually represents unused variables
departure, _, destination = "Montreal->Toronto".partition('->')
print("departure, destination:", departure, destination)

# use string.format function to print values easily
input_t = (1, 2)
print("Elements are {input_tuple[0]}, {input_tuple[1]}".format(input_tuple=input_t))
