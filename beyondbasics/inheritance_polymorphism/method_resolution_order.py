from pprint import pprint


class A:
    def func(self):
        return 'A func called'


class B(A):
    def func(self):
        return 'B func called'


class C(A):
    def func(self):
        return 'C func called'


class BC(B, C):
    pass


class CB(C, B):
    pass


# This class fail to compile because class A must be placed before B (as defined by Fail) and after B (as defined by B)
# class Fail(A, B):
#     pass


if __name__ == '__main__':
    # Class.__mro__ or Class.mro() returns method resolution order of class
    # Object is the ultimate base class of every class in Python
    pprint([' --- BC.mro() ---', BC.mro()])
    print('')
    pprint([' --- CB.mro() ---', CB.mro()])

    print('\nFunction "func" is resolved by the method resolution order (displayed above)')
    print('BC().func()', BC().func())
    print('CB().func()', CB().func())
