class ClassDecorator:
    """
    We can use classes as decorators as long as it implements __call__() method:
        ○ Classes are callable so they can be used as decorators
        ○ Calling classes produces a new instance of that class. Therefore, the resulting instance must also be callable
        ○ Therefore, __call__() must be implemented to meet the requirements
    """

    def __init__(self, func):
        """
        When a class is called as a decorator, a function is passed to the constructor, then to the initializer.
        Therefore, the first parameter of the initializer is the decorated function itself
        :param func: the decorated function
        """
        self._f = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        """
        __call__() must be implemented
        __call__() does the real job of modifying the behaviour of the decorated function
        In this case, the returned callable object will produce whatever the original function does.
        """
        self.count += 1
        return self._f(*args, **kwargs)


@ClassDecorator
def hello(name):
    print("Hello {}".format(name))


if __name__ == "__main__":
    # Only run these demo code if the file is executed, not when it's imported
    hello("Bill")
    hello("Anna")
    hello("Josh")
    hello("Kate")
    # The new object by the name "hello" is no longer a function.
    # It is a callable object (with additional attribute "count")
    print("hello.count:", hello.count)
    print("type(hello):", type(hello))
