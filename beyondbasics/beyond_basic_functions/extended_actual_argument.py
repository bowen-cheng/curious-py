# Extended call syntax allows us to use:
# * any iterable series (such as a tuple) to populate positional arguments
# * any mapping type (such as a dictionary) that has string keys to populate keyword arguments


def print_args(arg1, *args):
    print("arg1:", arg1)
    print("args:", args)


my_tuple = (1, 2, 3)

# my_tuple is passed as a single variable, not unpacked
print("--- print_args(my_tuple) ---")
print_args(my_tuple)

# The leading * unpacks the content of the tuple into an iterable series
print("\n--- print_args(*my_tuple) ---")
print_args(*my_tuple)

print("\n=========================\n")


def print_kwargs(red, **kwargs):
    print("red:", red)
    print("kwargs:", kwargs)


my_dict = {"red": 21, "green": 25, "blue": 66, "hue": 100}

# my_dict is passed as a single variable, not unpacked
print("--- print_kwargs(my_dict) ---")
print_kwargs(my_dict)

# The leading ** unpacks the content of the dictionary to populate keyword arguments
print("\n--- print_kwargs(**my_dict) ---")
print_kwargs(**my_dict)
