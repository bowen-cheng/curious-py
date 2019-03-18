from fractions import Fraction
from decimal import Decimal
from math import floor, ceil

if __name__ == '__main__':
    print(Fraction(2, 3))

    # print(Fraction(2, 0))  # zero division error
    print(Fraction(0.5))
    print(Fraction(0.1))  # wrong value
    print(Fraction('1.3'))
    print(Fraction(Decimal('0.1')))
    print(Fraction('0.1') + Fraction('0.1'))
    print(Fraction(3, 7) - Fraction(1, 7))
    print(Fraction(3, 7) * Fraction(1, 7))
    print(Fraction(3, 7) / Fraction(1, 7))
    print(Fraction(3, 7) // Fraction(1, 7))
    print(Fraction(3, 7) % Fraction(1, 7))
    print(floor(Fraction(2, 3)))
    print(ceil(Fraction(2, 3)))
