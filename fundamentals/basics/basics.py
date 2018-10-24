import math as m

print("------- Math -------")

print("abs() is a built-in function: ", abs(-34), "\n")

print("math.sqrt(4): ", m.sqrt(4))
print("math.pow(2, 3): ", m.pow(2, 3), "\n")

print("'// (or %)' - modulus, 4//3: ", 4 // 3)
print("'**' - exponent, 2//3: ", 2 ** 3, "\n")

print("0b prefix defines binary numbers, 0b10: ", 0b10)
print("0o prefix defines octal numbers, 0o10: ", 0o10)
print("0x prefix defines hex-decimal numbers, 0x10: ", 0x10, "\n")

print("int() can convert value to integer number, int('66'): ", int("66"))
print("int() can also convert non-decimal numbers, int('10010110101', 2): ", int(int("10010110101", 2)))
print("float() can convert value to floating point numbers, float('88.66'): ", float("88.66"))
print("'nan' (not a number) is a special floating point number , float('nan'): ", float("nan"))
print("'inf' and '-inf' are also special floating point numbers, float('-inf'): ", float("-inf"), "\n")

print("None is null/nil in Python", "\n")

print("------- bool -------")
print("bool() returns if given value is truthy or falthy")
print("Numbers: only 0 and 0.0 is falthy", "\nbool(0):", bool(0), "\nbool(0.0):", bool(0.0))
print("strings: only empty string is falthy", "\nbool(''):", bool(""), "\nbool('False')", bool("False"))
print("arrays: only empty array is falthy", "\nbool([]):", bool([]), "\nbool([1, 2])", bool([1, 2]), "\n")

print("------- Conditional statements -------")
# bool(...) can be omitted in if statement:
# if bool("eggs"):
if "eggs":
    print("fried eggs please")

exp = ""
if exp == "some val":
    print("True for the 1st condition\n")
elif exp == "some other val":
    print("True for the 2nd condition\n")
else:
    print("False for other conditions\n")

print("------- Loops -------")
print("while loop:")
counter = 6
while counter:
    print(counter)
    counter -= 1
    if counter == 2:
        break

print("\nfor loop:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\nfor loop with index:")
# We need the built in function enumerate() to get index in for loop
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit, sep=": ")
