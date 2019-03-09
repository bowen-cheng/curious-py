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


if __name__ == "__main__":
    # Only run these demo code if the file is executed, not when it's imported
    print("test('¥©çΩ≈'):", without_decorator('¥©çΩ≈'))
    print("test_decorator('¥©çΩ≈'):", with_decorator('¥©çΩ≈'))
