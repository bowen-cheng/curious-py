# set is unordered collection of unique, immutable objects

s = {1, 2, 3, 4, 5}
print("s = {1, 2, 3, 4, 5}", s)

# the set constructor can be used for shallow copying and creating new sets
s2 = set(s)
s3 = s2.copy()
print("\ns2 = set(s):", s2)
print("s3 = s.copy():", s3)
print("s2 is s:", s2 is s)
print("s3 is s:", s3 is s)

# use in and not in to test membership
print("\n-1 not in s:", -1 not in s)

# add() adds one element
s.add(6)
print("\ns.add(6):", s)
# update adds a iterable series of elements
s.update([7, 8, 9])
print("s.update([7, 8, 9]):", s)

# remove() results in a error if key is not in the set, discard() does not
# s.remove(-1) <- error, -1 not in the set
s.discard(-1)  # <- no error
s.discard(5)
print("s.discard(5):", s)

# convenient set algebra functions, more on docs
s4 = {1, 2, -1, -2, -3, -4, -5}
s.issubset(s4)
s.issuperset(s4)
s.union(s4)
s.difference(s4)
s.intersection(s4)
