from pprint import pprint

"""
Typical file use:
    f= open(...)
    work()
    f.close()

To also handle exceptions:
    try:
        f = open(...)
        work()
        f.close()
    except (Errors) as e:
        handle_error(e)
    finally:
        f.close()

with-block can cleanup resource with context-managers
And open(...) returns a context-manager
"""

# This example shows reading file. Writing file is the same
with open('sample.txt', mode='rt', encoding='utf-8') as file:
    pprint(["{}".format(line) for line in file])
    # The file is automatically closed at the end by the with block
