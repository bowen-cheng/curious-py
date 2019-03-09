from closures_decorators.decorators import function_decorator
from closures_decorators.decorators import Trace
from closures_decorators.decorators import ClassDecorator


@ClassDecorator
@Trace()
@function_decorator
def multiple_decorator(x):
    """
    Multiple decorators are processed one by one from bottom to top, passing each resulting callable to the next one
    """
    return x


if __name__ == "__main__":
    print(multiple_decorator("¥©çΩ≈"))
    print(multiple_decorator.count)  # count exists because the @ClassDecorator is the last decorator processed
