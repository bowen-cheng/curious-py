from beyond_basic_functions import Resolver

# Whenever we create a new object, we are actually calling the class
resolve = Resolver()


def sequence_class(immutable):
    if immutable:
        return tuple
    else:
        return list


s = sequence_class(True)
t = s('123456')  # s is now an alias for type (tuple)
print(type(t))  # prints <class 'tuple'>
