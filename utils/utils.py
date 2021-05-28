"""Contains used functions for the program."""


def isfloat(argument):
    """this function takes a value as argument,
    returns False if it is not a float, or True
    if the value is a Float or an integer"""
    try:
        float(argument)
    except ValueError:
        return False
    return True


def ispair(argument):
    """this function takes a value as argument,
    returns True if it is a pair number, or False"""
    if (argument % 2) == 0:
        return True
    else:
        return False
