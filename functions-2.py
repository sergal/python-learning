def addition(adder):
    """
    >>> add5 = addition(5)
    >>> add5(3)
    8
    >>> add5(8)
    13
    >>> add8 = addition(8)
    >>> add8(2)
    10
    >>> add8(4)
    12
    """
    def return_function(addest):
        return addest + adder
    
    return return_function

def addition_lambda(adder):
    """
    >>> add5 = addition_lambda(5)
    >>> add5(3)
    8
    >>> add5(8)
    13
    >>> add8 = addition_lambda(8)
    >>> add8(2)
    10
    >>> add8(4)
    12
    """
    return lambda x: x + adder

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)