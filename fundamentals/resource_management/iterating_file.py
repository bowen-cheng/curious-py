import sys


def run(filepath):
    """
    Treat content of a file as iterable and iterate through it
    :param filepath: File path
    """
    file = open(filepath, mode="rt", encoding="utf-8")
    for line in file:
        sys.stdout.write(line)
    file.close()


if __name__ == '__main__':
    # reads 1st commandline argument as file path
    # sys.argv[0] is not the path name. Explained in its doc.
    run(sys.argv[1])
