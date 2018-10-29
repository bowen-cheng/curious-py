#!/usr/local/bin/python3
from sys import stderr


def sqrt_alexandria(x):
    if x < 0:
        # raise exceptions using the raise keyword
        raise ValueError("Cannot compute square root of negative number {}".format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2
        i += 1
    return guess


def main():
    try:
        print(sqrt_alexandria(4))
        print(sqrt_alexandria(9))
        print(sqrt_alexandria(-1))
    except ValueError as e:
        print("Error while computing sqrt: {}".format(str(e)), file=stderr)
    finally:
        print("The finally block can be used for cleaning up if exception occurs")


# when this file is run directly (instead of being called), its __name__ attribute automatically get assigned "__main__"
if __name__ == '__main__':
    main()
