from typing import Callable


def first_name(name):
    """ Normal function statement """
    return name.split()[0]


# Lambdas are actually of type Callable
func1: Callable[[str, int], str] = lambda name, age, : name.split()[-1]
func2: Callable[[], None] = lambda: print("I take no arguments and products no returns")
# No return keyword is allowed in lambda expressions
func3: Callable[[], int] = lambda: 1  # returns 1

# the built-in callable() function can be used for determining if an object can be called
print("callable(first_name)", callable(first_name))
print("callable(func1)", callable(func1))
print("callable(func2)", callable(func2))
print("callable(3)", callable(3))
