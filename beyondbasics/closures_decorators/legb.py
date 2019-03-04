# Python looks up variables by the LEGB sequence: local > enclosing > global > built-in

a = "global"


def func():
    a = "enclosing"

    def local_func():
        a = "local"
        print("local_func:", a)
    local_func()
    print("enclosing func:", a)


func()
print("global:", a)
