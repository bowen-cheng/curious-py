# Comprehensions can contain multiple statements
# The next statements are nested inside the previous one
# Later statements can use variables declared in previous statements
from notes_utils import print_separator

print("Comprehension with multiple statements")

multi_statement = [x / (x - y) for x in range(10) if x > 8 for y in range(10) if x - y != 0]
print(multi_statement)

# More readable version:
multi_statement = [x / (x - y)
                   for x in range(10)
                   if x > 8
                   for y in range(10)
                   if x - y != 0]
print(multi_statement)

# Full version without using comprehension:
multi_statement = []
for x in range(10):
    if x > 8:
        for y in range(10):
            if x - y != 0:
                multi_statement.append(x / (x - y))
print(multi_statement)

print_separator()
print("Comprehension with nested comprehension")

multi_input = [[y * 3 for y in range(x)] for x in range(10)]

# Full version without using comprehension:
outer = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y * 3)
    outer.append(inner)

print(outer)
