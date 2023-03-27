import sys


argv = sys.argv
if __name__ == "__main__":
    if len(argv) is not 3 or argv[1].isdigit() is False \
            or argv[2].isdigit() is False:
        print("the programm takes two integers as argument")
    else:
        argv[1] = int(argv[1])
        argv[2] = int(argv[2])
        print("Sum:       ", argv[1] + argv[2])
        print("Differene: ", argv[1] - argv[2])
        print("Product:   ", argv[2] * argv[1])
        if argv[2] == 0:
            print("Quotient: ERROR (division by zero)")
        else:
            print("Quotient:  ", argv[1] / argv[2])
        if argv[2] == 0:
            print("Remainder: ERROR (modulo by zero)")
        else:
            print("Remainder:  ", argv[1] % argv[2])
