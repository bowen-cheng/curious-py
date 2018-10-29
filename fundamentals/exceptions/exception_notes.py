import sys


def convert(s):
    try:
        num = int(s)
        print('conversion succeeded:', num)
    except (ValueError, TypeError) as e:  # catch multiple exceptions and get a named reference of the exception
        num = -1
        print('conversion failed, {}'.format(str(e)), file=sys.stderr)  # use sys.stderr to print error style output
        # pass <- use pass keyword to avoid indentation error if nothing to do, no empty except block allowed in python
    return num


convert("123")
convert([1, 2, 3])
convert("abc")
