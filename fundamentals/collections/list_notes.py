# lists are heterogeneous mutable sequences

s = "show how to index into sequences".split()
print(s)

# For python sequences
# positive indexing starts from 0, counting from left to right (same as the other languages)
print("\nstr_list[5]:", s[5])
# negative indexing starts from -1, counting FROM RIGHT TO LEFT
print("str_list[-1]:", s[-1])

# slicing a sequence with ":"
print("\ns[1:5]:", s[1:5])
# Combining positive and negative indexing
print("s[1:-1]:", s[1:-1])
# Slicing up to (excluding) a index
print("s[:-1]:", s[:-1])
# Slicing from (including) a index
print("s[1:]:", s[1:])

# Different ways of SHALLOW copying lists
full_slice = s[:]
copied = s.copy()
via_constructor = list(s)

# Demonstrating shallow copy:
# when we slice, copy or list(), we ONLY DUPLICATED POINTERS, NEVER DUPLICATE THE OBJECTS
s2 = [[1, 2]] * 2
print("\ns2 = [[1, 2]] * 2:", s2)
s2[1].append(3)
print("s2[1].append(3):", s2)

# index() is used for finding the index of elements
w = "the quick brown fox jumps over the lazy dog".split()
print("\nw.index('fox'):", w.index('fox'))
# print(w.index("unicorn")) <- ValueError: 'unicorn' is not in list

# Determining if an element presents in a list
print("\n'the' in w:", 'the' in w)

# Counting occurrences in a list
print("\nw.count('the'):", w.count('the'))

# Removing elements by index with "del" keywords
print("\nw: ", w)
del w[1]
print("del w[1]:", w)

# Removing first occurrence by value with "seq.remove()"
print("\nw: ", w)
w.remove('the')
print("w.remove('the'):", w)

# Inserting elements with seq.insert(index, item)
w.insert(len(w), '!!!!')
print("\nw.insert(len(w), '!!!!'):", w)

# + sign produces a new list
l1 = [1, 2]
l2 = [3, 4]
l_plus = l1 + l2
print("\nl_plus:", l_plus)

# += sign or extend() modifies a list in place
l3 = [1, 2]
print("\nl3:", l3)
l3 += [3, 4]
l3.extend([5, 6])
print("""l3 += [3, 4]
l3.extend([5, 6])
l3:""", l3)

l4 = [3, 2, 1, 6, 5, 4]
print("\nl4:", l4)
l4.reverse()
print("l4.reverse():", l4)
l4.sort()
print("l4.sort():", l4)
l4.sort(reverse=True)
print("l4.sort(reverse=True):", l4)
l5 = ['aaa', 'aaaa', 'aa', 'aaaaa', 'a']
print("l5:", l5)
l5.sort(key=len)  # the sorting key is a callback function
print("l5.sort():", l5)

# similarly, sorted(l5) function does the same thing but returns the sorted list
#
