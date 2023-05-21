from  functools import reduce

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if len(iterable) == 0:
        return None
    elif len(iterable) == 1:
        return iterable[0]
    else:
        result = function_to_apply(iter)
    # for element in iterable:
    #     next(element)
    #     print(element)
    #     return function_to_apply()


if __name__ == "__main__":
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    print(reduce(lambda u, v: u + v, lst))