# Iterable protocol: can be called by iter() to get an iterator
# Iterator protocol: can be called by next() to fetch the next item

my_iterable = [1, 2, 3, 4]
my_iterator = iter(my_iterable)

print(my_iterator.__next__())
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# print(next(my_iterator))  # <- raises exception (StopIteration) when it reaches the end


def is_empty(iterable):
    i = iter(iterable)
    try:
        i.__next__()
        return False
    except StopIteration:
        return True


print(is_empty({}))
