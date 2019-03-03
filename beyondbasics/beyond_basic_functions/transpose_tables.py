from pprint import pprint

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

combined = [letters, numbers]
print("combined:")
pprint(combined, width=20)

print("----zipped_with_index----")

zipped_with_index = zip(combined[0], combined[1])  # manually select the inner lists with index
for item in zipped_with_index:
    print(item)

print("----zipped_with_star----")
zipped_with_star = zip(*combined)  # instead of suing indexes, we can just unpack the 2d array
for item in zipped_with_star:
    print(item)

print("---------")
pprint(list(zip(*combined)), width=20)
