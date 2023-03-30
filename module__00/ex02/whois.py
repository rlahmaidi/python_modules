import sys
#print(sys.argv[1])
print(type(sys.argv[1]))
#print(isinstance(sys.argv[1], type(sys.argv[1])))
if len(sys.argv) == 1:
    print("please provide an integer as an argument the programm")
    sys.exit()
elif len(sys.argv) > 2:
     print("AssertionError: more than one argument are provided")
     sys.exit()
elif isinstance(sys.argv[1], int)== False:
    print("AssertionError: argument is not an integer")
    sys.exit()
elif int(sys.argv[1])  == 0 :
    print("I'm Zero")
elif int(sys.argv[1]) % 2 == 0 :
    print("I'm Even")
elif int(sys.argv[1]) % 2 != 0 :
    print("I'm Odd")

    ###############problem with isinstance() ############