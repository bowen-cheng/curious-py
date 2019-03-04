def sort_by_last_letter(strings):
    # last_letter("123")  # doesn't work, function not yet defined
    def last_letter(s):
        """
        * Functions can be defined inside another function
        * The local function is local to each instance of the outer function
        * The local functions are local name bindings in the function body
        * The local function cannot be called by sort_by_last_letter.last_letter() since it only exists when
          sort_by_last_letter is executed
        """
        return s[-1]
    print("last_letter", last_letter)  # prints different address each time the outer function is called
    return sorted(strings, key=last_letter)  # the inner function is passed as a reference


# sort_by_last_letter.last_letter('qwe')  # doesnt' work
sort_by_last_letter(['ddd', 'adf', 'qwe', 'xls'])
sort_by_last_letter(['ddd', 'adf', 'qwe', 'xls'])
sort_by_last_letter(['ddd', 'adf', 'qwe', 'xls'])


def outer():

    def local_func():
        print("local function")

    # local function can be treated just like any other objects, e.g. returned and passed around
    return local_func


print("\n--------------\n")

local_func_ref = outer()
local_func_ref()
