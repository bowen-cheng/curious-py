# Python uses dynamic type system. Object types are only resolved at runtime.
def my_add(a, b):
    print(a + b)


my_add("Pyt", "hon")
my_add(1, 2)
my_add([1, 2], [3])
# my_add("abc", 56) <- TypeError: can only concatenate str (not "int") to str

