from collections import Iterable

def additions(values_list):
    """
    >>> adds = additions(range(3))
    >>> adds[0](1)
    1
    >>> adds[1](1)
    2
    >>> adds[2](1)
    3
    """
    if not isinstance(values_list, Iterable):
        values_list = [values_list]    

    def res_function(adder):
        return lambda x: x + adder

    return map(lambda value: res_function(value), values_list)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)    