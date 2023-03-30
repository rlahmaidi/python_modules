import sys
import string


def text_analyzer(text=None):
    '''
    This function counts the number of upper characters, lower characters,

    punctuation and spaces in a given text.

    '''
    #  second condition : when user hit enter with no input
    while (text is None or text == ""):
        text = input("What is the text to analyze?\n")
    if isinstance(text, str) is False:
        print("AssertionError: argument is not a string")
    else:
        punctuation = string.punctuation
        upp = 0
        low = 0
        punc = 0
        for i in text:
            if 'A' <= i and 'Z' >= i:
                upp += 1
            elif 'a' <= i and 'z' >= i:
                low += 1
            elif i in punctuation:
                punc += 1
        print("The text contains", len(text), "character(s):")
        print("-", upp, "upper letter(s)")
        print("-", low, "lower letter(s)")
        print("-", punc, "punctuation mark(s)")
    return


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("the programm takes only one argument")
    else:
        text_analyzer(sys.argv[1])
