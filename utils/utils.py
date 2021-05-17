"""Docstrings."""


def isfloat(str):
    try:
        float(str)
    except ValueError:
        return False
    return True
