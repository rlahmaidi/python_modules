# def myFun(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
 
 
# # Now we can use *args or **kwargs to
# # pass arguments to this function :
# args = ("Geeks", "for", "Geeks")
# myFun(*args)
 
# kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks", "tmp": "tmpe"}
# myFun(**kwargs)
# def myfun(*args):
#     for arg in args:
#         print(arg)

# def myfun2(*args,**kwargs):
#     print("those are non keyword arguments")
#     for i in args:
#         print(i)
#     print("the below are keyword arguments")
#     for key,value in kwargs.items():
#         print(key, " = ", value)


# myfun2("something","not something",name="rachid", second_name="", third_name="elidrissi")

lst = ["a","b","d"]
name = "var_"
for count,el in enumerate(lst):
    print(name + str(count))