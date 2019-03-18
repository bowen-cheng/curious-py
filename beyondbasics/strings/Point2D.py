class Point1D:
    def __init__(self, x):
        self.x = x


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """
        Supports str(object) method
        str() produces a readable, human-friendly representation of an object (not programmer orientated)
        By default, str() simply calls repr()
        str() is for clients
        """
        return "({}, {}) __str__".format(self.x, self.y)

    def __repr__(self):
        """
        Supports repr(object) method
        repr() produces and unambiguous string representation of an object
        the result of repr() should contain more information than the result of str()
        always write a repr() for your classes (The default implementation is not useful)
        repr() is used when showing elements of a collection
        repr() is for developers
        """
        return "Point2D(x={}, y={}) __repr__".format(self.x, self.y)

    def __format__(self, format_spec):
        """
        Supports "{}".format(Point2D(1, 2))
        By default, __format__() calls __str__
        :param format_spec:
        :return:
        """
        return "[Formatted point: {}, {}, {}]".format(self.x, self.y, format_spec)


if __name__ == "__main__":
    p1 = Point1D(26)
    print("repr(p1):", repr(p1))
    print("str(p1):", str(p1))
    print("\n")
    p2 = Point2D(26, 28)
    print("repr(p2):", repr(p2))
    print("str(p2):", str(p2))
    print("\n")
    print("This is a point: {}".format(p2))
