# class HelloContextManager:
#      def __enter__(self):
#          print("Entering the context")
#          return "Hello, World!"
#      def __exit__(self, exc_type, exc_value, exc_tb):
#          print("Leaving the context")
#          print(exc_type, exc_value, exc_tb, sep="\n")


# # with HelloContextManager() as hello:
# #      print(hello)
# with HelloContextManager() as hello:
#     print(hello)
#     hello[100]
# class test:
#     pass

# tmp = test()
# tmp.__setattr__("name", "rachid")
# print(tmp.name)

st = "\nrachid,"
sp = st.split(",")
# sp = [1,2,3,4]
# print(sp)
# if '' in sp:
#     print("yes")
# else:
#     print("no")
tmp = st.strip()
print(st)
print(tmp)