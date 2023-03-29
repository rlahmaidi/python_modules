import sys
import string


# def is_string_got_lentgh(x,N):
#     if len(x) > N:
#         return True
#     return False

argv = sys.argv
if __name__ == "__main__":
    if len(sys.argv) is not 3 or argv[2].isdigit() is False or argv[1].isdigit() is True:
        print("ERROR")
    else:
        N = int(argv[2])
        punc = string.punctuation
        for i in argv[1]:
            if i in punc:
                argv[1] = argv[1].replace(i, '')
        lst = argv[1].split()
        lst1 =  [ x for x in lst if len(x) > N]
        print(lst1)
       