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
            return func(*args, **kwargs)

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
