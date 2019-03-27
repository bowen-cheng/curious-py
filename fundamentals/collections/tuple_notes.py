# tuples are heterogeneous immutable sequence.
# Once created, the objects within them cannot be replaced or removed and new elements cannot be added.

from notes_utils import print_items

# tuples are defined by "(", ")" and ","
t = ("\nstring", 4.3, 6)

# tuple elements can be accessed by index
print("\nt[0]", t[0])

# len() function returns length of a tuple
print("\nlen(t)", len(t))

# tuple elements can be looped over
print("\nfor in loop on tuple")
print_items(t)

# + sign can be used for concatenating tuples
t_concat = t + ("new_1", "new_2")
print('\nt_concat = t + ("new_1", "new_2")')
print_items(t_concat)

# * sign can be used for repeating tuples
t_repeat = t * 2
print("\nt_repeat = t * 2")
print_items(t_repeat)

# tuples can be nested with each other
t_nested = ((1, 2), ('a', 'b'), (2.5, 3))
print("\nt_nested[0][0]:", t_nested[0][0])
print("t_nested[1][1]:", t_nested[1][1])

# tuples with a single value must end with ","
print("\ntype((6,)):", type((6,)))
print("type(6):", type(6))


# tuples allows functions to return multiple values
def min_max(array_input):
    # the surrounding parentheses of tuples can be omitted
    return min(array_input), max(array_input)


# tuple unpacking allows us to destruct tuple values into named references
min_val, max_val = min_max([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("\nmin_val, max_val = min_max([1, 2, 3, 4, 5, 6, 7, 8, 9])")
print("min_val, max_val:", min_val, max_val)

# unpacking tuple into named references
(a, (b, (c, d))) = (1, (2, (3, 4)))
print("\n(a, (b, (c, d))) = (1, (2, (3, 4)))")
print("a,b,c,d: ", a, b, c, d)

# idiomatic Python swap
print("\na, b:", a, b)
print("a, b = b, a")
a, b = b, a
print("a, b:", a, b)

# tuple constructor can create tuples from any iterable series
t_array = tuple([1, 2, 3, 4, 5, 6])
print("\ntuple([1, 2, 3, 4, 5, 6])")
print_items(t_array)
t_string = tuple('Michael')
print("tuple('Michael')")
print_items(t_string)

# in and not in operator can be used for membership testing for any collection types (including tuple)
print("\n6 in (1, 2, 3, 4, 5, 6):", 6 in (1, 2, 3, 4, 5, 6))
print("7 not in (1, 2, 3, 4, 5, 6):", 7 not in (1, 2, 3, 4, 5, 6))
