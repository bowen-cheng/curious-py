# All generators are iterable sequences (iterators)
#   lazily evaluated, the next value is computed on demand
#   can model infinite sequences, such as data streams with no definite end
#   are composable into pipelines for natural stream processing

# A generator function is defined by any Python function that uses the "yield" keyword at least once.
# It can also contain return keyword without argument


def gen123():
    """
    Each time next() is called, the function runs up to and including the yield statement
    The state of the function is “saved” from the last call and can be picked up the next time
    :return:
    """
    print('about to yield 1')
    yield 1
    print('about to yield 2')
    yield 2
    print('about to yield 3')
    yield 3
    print('about to return')


g = gen123()
print("next(g):", next(g))  # prints 1
print("next(g):", next(g))  # prints 2
print("next(g):", next(g))  # prints 3
# print(next(g))  # prints 'about to return' and throws StopIteration exception

# can work with for loop since it is a sequence
print('\nfor i in gen123(): print(i):')
for i in gen123():
    print(i)
