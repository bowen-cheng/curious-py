def enclosing():
    x = "text in the enclosing function scope"

    def local_function():
        # This local function needs a variable from its enclosing scope
        print("local function :", x)

    return local_function


# This local functions can still work perfectly fine even in a scope that no longer exists
# Why? This is because Python forms closures for such functions.
# The closure essentially remembers the object from the enclosing scope that the local function needs.
# They are stored in attribute __closure__
lf = enclosing()
lf()
print("\nlf.__closure__:", lf.__closure__)
