import functools


def do_nothing(f):
    @functools.wraps(f)  # functools.wraps maintains the metadata of the decorated function
    def my_wrap():
        print("my_wrap called")
        return f()

    return my_wrap


@do_nothing
def hello():
    """ Some documentation here """
    print("Hello world")


# without @functools.wraps(f)
# >>> from closures_decorators.decorators.functools_wraps import hello
# >>> hello.__doc__
# >>>
# >>> hello.__name__
# >>> 'my_wrap'


# with @functools.wraps(f)
# >>> from closures_decorators.decorators.functools_wraps import hello
# >>> hello.__doc__
# >>> Some documentation here
# >>> hello.__name__
# >>> 'hello'
