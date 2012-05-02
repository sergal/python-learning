from collections import Iterable

def f(*data):
    """
    >>> f(1, 2, 3)
    6
    >>> f([1, 2, 3])
    6
    >>> f((3, 5, 6))
    14
    >>> f(3, (5, 6))
    14
    """
    result = 0
    for elem in data:
        if isinstance(elem, Iterable):
            result += f(*elem)
        else:
            result += elem

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)