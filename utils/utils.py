"""Docstrings."""


def isfloat(argument):
    """[summary]

    Args:
        str ([type]): [description]

    Returns:
        [type]: [description]
    """
    try:
        float(argument)
    except ValueError:
        return False
    return True
