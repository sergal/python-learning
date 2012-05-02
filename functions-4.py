from collections import Iterable

def mymap(func, args):
    """
    >>> plus1 = lambda x: x+1 
    >>> minus1 = lambda x: x-1
    >>> mymap(plus1, 1)
    [2]
    >>> mymap([plus1, minus1], [1,2])
    [2, 1]
    """
    if not isinstance(func, Iterable):
        func = [func]
        args = [args]

    res = []
    for index, item in enumerate(func):
        res.append(item(args[index]))

    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)        