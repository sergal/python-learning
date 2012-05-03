from collections import Iterator

def chain(*args):
    """
    >>> i1 = iter([1, 2, 3])
    >>> i2 = iter([4, 5])
    >>> c = chain(i1, i2)
    >>> c.next()
    1
    >>> c.next()
    2
    >>> c.next()
    3
    >>> c.next()
    4
    >>> c.next()
    5
    """
    for arg in args:
        if not isinstance(arg, Iterator):
            raise TypeError

    for arg in args:
        try:
            while True:
                yield arg.next()
        except StopIteration:
            pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)            