#!/usr/local/bin/python3
# each Python file is a module


# A function that doesn't have a return statement implicitly returns None
def launch_missile():
    print("missile launched!")


# Two lines between each function is preferred
# Python doc is written within the function, not above it
def even_or_odd(number):
    """
    Determines if a give number is odd or even
    :param number: the input number
    :return: even or odd
    """
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


# When this file is directly executed, the "__name__" attribute of this module automatically has value "__main__"
if __name__ == "__main__":
    # call a list of functions here
    print("I'm being executed as a program")
