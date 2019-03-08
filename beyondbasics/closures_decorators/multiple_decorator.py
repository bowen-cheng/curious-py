from closures_decorators.function_decorators import function_decorator
from closures_decorators.instance_decorator import Trace
from closures_decorators.class_decorator import ClassDecorator

tracer = Trace()


@ClassDecorator
@tracer
@function_decorator
def multiple_decorator(x):
    """
    Multiple decorators are processed one by one from bottom to top, passing each resulting callable to the next one
    """
    return x


print(multiple_decorator("¥©çΩ≈"))
print(multiple_decorator.count)  # count exists because the @ClassDecorator is the last decorator processed
print("\n------------------\n")
