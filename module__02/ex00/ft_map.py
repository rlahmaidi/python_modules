from collections.abc import Iterable


def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if not isinstance(iterable, Iterable):
        raise TypeError(type(iterable), "object is not iterable")
    for element in iterable:
        # print(function_to_apply(element))
        yield function_to_apply(element)


def double_number(n):
    return n * 2


if __name__ == "__main__":
    x = (1, 2, 3, 4, 5)
    print(ft_map(lambda dum: dum + 1, x))
    print(list(ft_map(lambda t: t + 1, x)))
    print(list(ft_map(double_number, x)))
    print("@@@@@@@@ exceptions @@@@@@")
    x = 1
    print(list(map(lambda t: t + 1, x)))
    print(list(ft_map(double_number, x)))
