from functools import reduce
from collections.abc import Iterable


def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if not isinstance(iterable, Iterable):
        raise TypeError("reduce() arg 2 must support iteration")
    if not iterable:
        raise TypeError("reduce() of empty iterable with no initial value")
    if len(iterable) == 0:
        return None
    elif len(iterable) == 1:
        return iterable[0]
    else:
        result = iterable[0]
        for i in range(1, len(iterable)):
            result = function_to_apply(result, iterable[i])
        return result


if __name__ == "__main__":
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    intergers = [0, 1, 2, 3]
    empty = []
    x = 0
    print("theirs: ", reduce(lambda u, v: u + v, lst))
    print("my own: ", ft_reduce(lambda u, v: u + v, lst))
    print("theirs: ", reduce(lambda u, v: v * 2, intergers))
    print("my own: ", ft_reduce(lambda u, v: v * 2, intergers))
    print("@@@@@@@@@@@@ exceptions @@@@@@@@")
    print("non iterable object: ")
    print("theirs: ", reduce(lambda u, v: u + v, x))
    print("my own: ", ft_reduce(lambda u, v: u + v, x))
    print("empty iterable")
    print("theirs: ", reduce(lambda u, v: u + v, empty))
    print("my own: ", ft_reduce(lambda u, v: u + v, empty))
