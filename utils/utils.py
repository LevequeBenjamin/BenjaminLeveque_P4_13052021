"""Contains used functions for the program."""


def isfloat(argument):
    """this function takes a value as argument,
    returns Flase if it is not a float, and True
    if the value is a Float or an integer"""
    try:
        float(argument)
    except ValueError:
        return False
    return True


def ispair(argument):
    if (argument % 2) == 0:
        return True
    else:
        return False
