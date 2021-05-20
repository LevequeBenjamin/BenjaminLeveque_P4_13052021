"""Docstrings."""


def isfloat(str):
    """[summary]

    Args:
        str ([type]): [description]

    Returns:
        [type]: [description]
    """
    try:
        float(str)
    except ValueError:
        return False
    return True
