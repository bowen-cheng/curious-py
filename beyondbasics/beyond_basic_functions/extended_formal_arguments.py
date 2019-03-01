def extended_args(positional_1, positional_2, *args, named_1, named_2, **kwargs):
    """
    * All of the arguments are optional and can be omitted when declaring a function
    * The above declaration order of extended arguments must be maintained
    :param positional_1: 1st positional argument
    :param positional_2: 2nd positional argument
    :param args: variable length "list" of positional argument, can be renamed
    :param named_1: 1st named argument
    :param named_2: 2nd named argument
    :param kwargs: variable length "dictionary" of named argument, can be renamed
    """
    print("positional_1: ", positional_1)
    print("positional_2: ", positional_2)

    if args:
        print("*args:", args)

    print("named_1", named_1)
    print("named_2", named_2)

    if kwargs:
        print("Followings are kwargs:")
        for key, value in kwargs.items():
            print("{} -> {}".format(key, value))


extended_args(1, 2, 3, 4, 5, named_1='a', named_2='b', named_3=10, named_4=20)
