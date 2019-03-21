class Base:
    def __init__(self):
        print('Base initializer')

    def func(self):
        print('Base.func()')


class Sub(Base):
    def __init__(self):
        """
        Sub classes should call the initializer of super class (though not mandatory)
        Base class initializer will ONLY be called AUTOMATICALLY if subclass initializer is undefined
        """
        super().__init__()
        print('Sub-class initializer')

    def func(self):
        print('Sub.func()')


class SubEmpty(Base):
    pass


if __name__ == '__main__':
    print('=====================')
    sub = Sub()
    sub.func()

    print('=====================')
    sub_empty = SubEmpty()
    sub_empty.func()
