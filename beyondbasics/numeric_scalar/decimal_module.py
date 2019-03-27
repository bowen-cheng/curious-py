from notes_utils import print_separator
from decimal import Decimal
import decimal

if __name__ == "__main__":
    # Always quote literal fractional values for math operations
    print(Decimal(0.8) - Decimal(0.7))
    print(Decimal('0.8') - Decimal('0.7'))

    print_separator()
    # This forces the decimal class to create decimals from quoted literals
    decimal.getcontext().traps[decimal.FloatOperation] = True
    # Decimal(0.9)  # error
    print(Decimal('0.6'))

    print_separator()
    # Set the precision to 6 digits
    decimal.getcontext().prec = 6
    print(Decimal('1.1234567') + 1)

    print_separator()
    print(Decimal('Infinity'))
    print(Decimal('-Infinity'))
    print(Decimal('NaN'))
    print(Decimal('NaN') + Decimal('1.09'))
    print(Decimal('Infinity') + Decimal('1.09'))

    print_separator()
    print((-7) % 3)
    print(Decimal('-7') % Decimal('3'))

    print_separator()
    print((-7) // 3)
    print(Decimal('-7') // Decimal('3'))
