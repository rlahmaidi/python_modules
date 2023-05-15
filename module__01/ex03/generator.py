import sys
import random
import string


def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings
     before it is yielded.
    '''
    if not isinstance(text, str) or not text.isprintable():
        print("this function accept only text with printable characters")
        sys.exit()
    else:
        lst = text.split(sep)
        if option == "shuffle":
            random.shuffle(lst)
            for element in lst:
                yield element
        elif option == "unique":
            unique = set(lst)
            for element in unique:
                yield element
        elif option == "ordered":
            lst.sort()
            for element in lst:
                yield element
        else:
            for element in lst:
                yield element


text = "dangalo bangalo my sorted my sengalo my sorted"
it = generator(text, "my", "unique")
# print(next(it))
# print(next(it))
# print(next(it))
