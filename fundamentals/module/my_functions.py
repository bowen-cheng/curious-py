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


print("If you see this, it means I'm being imported, my __name__ = ", __name__)

if __name__ == "__main__":
    """
    * When this file is directly executed, the "__name__" attribute of this module automatically has value "__main__"
    * When this file is imported its __name__ attribute is "fundamentals.module.my_functions"
    * If the following print statement is not placed in the "if __name__ == '__main__'" block, it will be executed when
      this module is imported
    """
    # call a list of functions here
    print("I'm being executed as a program")
    print("My __name__ attr has value:", __name__)
