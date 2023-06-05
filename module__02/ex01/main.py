def what_are_the_vars(*args, **kwargs):
    """
    this function return a ObjectC object instanciated  via
    the parameters recieved as arguments
    """
    obj = ObjectC()
    i = 0
    for argument in args:
        name = "var_"
        setattr(obj, name + str(i), argument)
        i += 1
    for key, value in kwargs.items():
        if getattr(obj, key, -1) != -1:
            return None
        setattr(obj, key, value)
    return(obj)
# To remember in correction:
# 1- the above return None was done based on a test in the subject
# they don't want us to overide an already seeted variable
# 2- the last test should print var_0:42 not 12, they confirm it in discord


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    print("the error should be printed now")
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)
