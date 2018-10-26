def print_list(input_list):
    for val in input_list:
        print(val)


# All variables are named references to objects
a = [1, 2, 3]
# This does not copy the actual list object
b = a
# This actually modifies the underlying object
b[0] = 4
# prints 4, 2, 3 because a and b points to the same underlying object
print_list(a)
# prints True since id() deals with object and a and b are just named references to the same object
print(id(a) == id(b))


# same case in function call: pass by reference
def modify_argument(argument, my_sep="------"):
    # Actually modifying the same object as a (the argument) is pointing to
    argument[0] = 100
    # prints 100, 2, 3
    print(my_sep)
    print_list(a)
    print(my_sep)


# if we use named argument, we can specify the arguments in any order
modify_argument(my_sep="******", argument=a)


# default arguments values are evaluated when def is evaluated.
# They can be modified like any other objects
# Keep in mind they are OBJECTS (the above rules hold).
def append_word(words=[]):
    words.append("Python")
    print(words)


# prints:
# ['Python']
# ['Python', 'Python']
# ['Python', 'Python', 'Python']
# since the default argument is reused each time
append_word()
append_word()
append_word()
