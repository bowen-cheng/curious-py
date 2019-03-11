def check_non_negative(index):
    """ check_non_negative is not a decorator at all since it takes a number not a callable """
    def validator(f):
        """ I'm the real decorator! And I closes over the index variable! """
        def wrap(*args):
            if args[index] < 0:
                raise ValueError("Argument {} cannot be negative".format(index))
            return f(*args)

        return wrap
    return validator


# check_non_negative is not the real decorator, but its return value is!
# The real decorator here is actually the returned function of check_non_negative(1).
# Note that check_non_negative is actually called with parameter of value = 1
@check_non_negative(1)  # The 2nd parameter cannot be negative
def create_list(value, size):
    return [value] * size


# The above example is actually equivalent to the following:
dec_func = check_non_negative(1) # This is the real decorator function
@dec_func
def create_list_full(value, size):
    return [value] * size


if __name__ == "__main__":
    # create_list(6, -6)  # same result as create_list_full(6, -6)
    create_list_full(6, -6)
