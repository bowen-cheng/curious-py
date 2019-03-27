# range is a type of sequence used for representing arithmetic progression of integers
from notes_utils import print_items

# ranges are created by calling range constructor range(start_val, stop_val)
print("range(0, 5):")
print_items(range(0, 5))

# the start value can be omitted, but not the stop value
print("range(2):")
print_items(range(2))

# if we want to provide a step value, then all three parameters must all be provided
print("range(0, 10, 2):")
print_items(range(0, 10, 2))
