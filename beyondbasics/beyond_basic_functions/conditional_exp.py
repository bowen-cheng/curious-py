def is_even_statement(param):
    """ This is the if statement, nothing fancy here """
    if param % 2 == 0:
        return True
    else:
        return False


def is_even_expression(parm):
    """
    The conditional expression is a lot more simpler and readable:
        result = true_val if condition else false_val
    """
    result = True if parm % 2 == 0 else False
    return result
