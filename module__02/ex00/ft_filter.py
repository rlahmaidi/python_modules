from collections.abc import Iterable


def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
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
        if function_to_apply(element):
            yield element


def divise_two(dum):
    if dum % 2 == 0:
        return True
    else:
        return False


# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    print(ft_filter(divise_two, x))
    print(list(ft_filter(divise_two, x)))
    print(list(filter(lambda dum: not (dum % 2), x)))

    sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
    filtered = ft_filter(fun, sequence)

    print('The filtered letters are:')
    for s in filtered:
        print(s)
    print("@@@@@@@@@@ exceptins @@@@@@@")
    x = 0
    print("not iterable exception: ")
    print("theirs: ", list(filter(divise_two, x)))
    print(list(ft_filter(divise_two, x)))
