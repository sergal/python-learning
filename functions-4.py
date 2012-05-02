from collections import Iterable

def mymap(func, args):
    """
    >>> plus1 = lambda x: x+1 
    >>> minus1 = lambda x: x-1
    >>> mymap(plus1, 1)
    [2]
    >>> mymap(plus1, [1,3])
    [(2, 4)]
    >>> mymap([plus1, minus1], [1,2])
    [(2, 3), (0, 1)]
    """
    if not isinstance(func, Iterable):
        func = [func]

    if not isinstance(args, Iterable):
        args = [args]

    res = []
    for f in func:
        tempres = []
        for arg in args:
            tempres.append(f(arg))
        if len(tempres) > 1:
            tempres = tuple(tempres)
        else:
            tempres = tempres[0]
        res.append(tempres)

    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)        