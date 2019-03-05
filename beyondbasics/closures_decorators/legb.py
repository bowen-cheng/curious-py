# Python looks up variables by the LEGB sequence: local > enclosing > global > built-in
# However, this rule DOES NOT apply when binding new name spaces:
#   e.g. defining new variables with the same name but in different scopes
# keyword "global" and "nonlocal" can be used for re-binding variables in global and enclosing scope

a = "global_a"


def func():
    # Note that this does NOT over-write the value of var a in the global scope
    a = "enclosing_a"
    print("enclosing func:", a)

    def local_func():
        # Note that this does NOT over-write the value of var a in the enclosing scope or global scope
        a = "local_a"
        print("local_func:", a)

    local_func()


print("global:", a)
func()

print("\n-------------\n")
b = "global_b"


def func2():
    # the global keyword can be used for changing the value of var b in the global scope
    global b
    b = "enclosing_b"
    c = "enclosing_c"
    print("enclosing func2, global b:", b)
    print("enclosing func2, c", c)

    def local_func2():
        # the nonlocal keyword can be used for changing the value of var c in the enclosing scope
        nonlocal c
        c = "local_c"
        print("local_func2, nonlocal c:", c)

    local_func2()


print("global:", b)
func2()
