from collections import Iterator
import itertools

def cycle(iter):
    """
    >>> i = iter([1, 2, 3])
    >>> c = cycle(i)
    >>> c.next()
    1
    >>> c.next()
    2
    >>> c.next()
    3
    >>> c.next()
    1
    """
    if not isinstance(iter, Iterator):
        raise TypeError

    return itertools.cycle(iter)

def cycle2(iter):
    """
    >>> i = iter([1, 2, 3])
    >>> c = cycle(i)
    >>> c.next()
    1
    >>> c.next()
    2
    >>> c.next()
    3
    >>> c.next()
    1
    """
    if not isinstance(iter, Iterator):
        raise TypeError

    l = [a for a in iter]
    while True:
        for elem in l:
            yield elem

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)            