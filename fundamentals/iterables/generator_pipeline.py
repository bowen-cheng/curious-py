#!/usr/local/bin/python3


def take(count, iterable):
    """
    Yield the first given number of elements from an iterable series
    :param count:
    :param iterable:
    :return:
    """
    taken = 0
    for item in iterable:
        if taken >= count:
            return
        yield item
        taken += 1


def distinct(iterable):
    """
    Yield all distinct elements from an iterable series
    :param iterable:
    :return:
    """
    seen = set()
    for item in iterable:
        if seen.__contains__(item):
            continue
        else:
            seen.add(item)
            yield item


def gen_pipe():
    print("Taking the first 3 unique element from ['a', 'a', 'a', 'b', 'b', 'c', 'd', 'd', 'd']")
    print("take(3, distinct(my_arr)):")
    my_arr = ['a', 'a', 'a', 'b', 'b', 'c', 'd', 'd', 'd']
    unique_generator = take(3, distinct(my_arr))
    for item in unique_generator:
        print(item)


if __name__ == '__main__':
    gen_pipe()
