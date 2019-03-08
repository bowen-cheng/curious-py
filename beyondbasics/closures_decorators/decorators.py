def function_decorator(decorated_func):
    """
    This function can be used as a decorator since it takes a callable and returns a callable
    :param decorated_func: the original input function
    :return: a modified function that binds to the name of the original function
    """

    def wrap(*args, **kwargs):
        # Further modify the output of original function
        original_output = decorated_func(*args, **kwargs)
        return ascii(original_output)

    return wrap


def without_decorator(x):
    return x


@function_decorator
def with_decorator(x):
    return x


print("test('¥©çΩ≈'):", without_decorator('¥©çΩ≈'))
print("test_decorator('¥©çΩ≈'):", with_decorator('¥©çΩ≈'))
print("\n------------------\n")


class ClassDecorator:
    """
    • We can use classes as decorators as long as it implements __call__() method:
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


hello("Bill")
hello("Anna")
hello("Josh")
hello("Kate")
# The new object by the name "hello" is no longer a function.
# It is a callable object (with additional attribute "count")
print("hello.count:", hello.count)
print("type(hello):", type(hello))
print("type(without_decorator):", type(without_decorator))

print("\n------------------\n")


class Trace:
    def __init__(self):
        """
        A parameter for the decorated function is not needed here because the decorator itself is an created instance
        Its constructor and initializer will have been called by the time it modifies the decorated function
        """
        self.enabled = True

    def __call__(self, func):
        """
        A parameter for the decorated function is present here because the __call__() method is executed whenever a
        callable instance is executed.
        :param func:
        :return:
        """

        def wrap(*args, **kwargs):
            if self.enabled:
                print("Tracing: calling {}".format(func))
            func(*args, **kwargs)

        return wrap


tracer = Trace()


@Trace()  # note the trailing () when using instance decorator vs class decorator
def print_words():
    print("A Star is Born")


@tracer  # This works too
def print_words2():
    print("A Star is Born")


print_words()
print_words2()
