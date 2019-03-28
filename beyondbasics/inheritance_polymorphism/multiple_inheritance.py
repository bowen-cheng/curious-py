from pprint import pprint


class SimpleList:
    def __init__(self, items):
        print('SimpleList initialized')
        self._items = list(items)

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return 'SimpleList({!r})'.format(self._items)

    def add(self, item):
        self._items.append(item)

    def sort(self):
        self._items.sort()


class SortedList(SimpleList):
    def __init__(self, items=()):
        print('SortedList initialized')
        super().__init__(items)
        self.sort()

    def __repr__(self):
        return 'SortedList({!r})'.format(list(self))

    def add(self, item):
        super().add(item)
        self.sort()


class IntList(SimpleList):
    def __init__(self, items=()):
        print('IntList initialized')
        for x in items:
            self._validate(x)
        super().__init__(items)

    def __repr__(self):
        return 'IntList({!r})'.format(list(self))

    @staticmethod
    def _validate(x):
        # The built-in isinstance() method does the type check
        if not isinstance(x, int):
            raise ValueError('"IntList" only supports integer values.')

    def add(self, item):
        self._validate(item)
        # Depending on the calling context, this super() doesn't necessarily refer to the same class! (Unlike Java)
        super().add(item)


class SortedIntList(IntList, SortedList):
    """
    If a class
        1. has multiple base classes
        2. defines no initializer
    Then only the initializer of the first bse class is automatically called
    """
    def __repr__(self):
        return 'SortedIntList({!r})'.format(list(self))


if __name__ == '__main__':
    print('\n--- SortedList ---')
    sorted_list = SortedList()
    sorted_list.add(10)
    sorted_list.add(-10)
    sorted_list.add(20)
    print(sorted_list)

    print('\n--- IntList ---')
    int_list = IntList()
    int_list.add(1)
    int_list.add(2)
    # int_list.add('a')  # Raises ValueError, only numbers are allowed
    print(int_list)

    print('\n--- SortedIntList ---')
    sorted_int_list = SortedIntList()
    sorted_int_list.add(10)
    sorted_int_list.add(-10)
    sorted_int_list.add(20)
    # sorted_int_list.add('abc')  # Raises ValueError, only numbers are allowed
    print(sorted_int_list)

    print('\n--- isinstance ---')
    print('isinstance(sorted_list, SortedList)', isinstance(sorted_list, SortedList))

    print('\n--- issubclass ---')
    print('issubclass(IntList, SimpleList)', issubclass(IntList, SimpleList))

    print('\n--- Class.__base__ ---')
    # Class.__base__ returns a tuple of base classes
    print('IntList.__bases__', IntList.__bases__)
    print('SortedIntList.__bases__', SortedIntList.__bases__)

    print('\n--- Class.__mro__ ---')
    # Class.__mro__ or Class.mro() returns method resolution order of class
    pprint([' --- IntList.mro() ---', IntList.mro()], width=40)
    print('')
    pprint([' --- SortedIntList.mro() ---', SortedIntList.mro()])

    print('\n--- super(...) proxy object ---')
    # SortedIntList works because add() method always call super().add(...), see notes for more
    print('Instance-bound proxy:')
    print('super(SortedList, sorted_int_list).add', super(SortedList, sorted_int_list).add)
    print('Class-bound proxy:')
    print('super(SortedList, SortedIntList).add', super(SortedList, SortedIntList).add)
