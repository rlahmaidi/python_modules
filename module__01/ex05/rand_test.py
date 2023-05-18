# class test:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
    

# t = test("rachid", 1)
# if isinstance(t, test):
#     print("yes, this is a test instance(object)")
# else:
#     print("no")
# lst = ["a", "b", "c"]
# if "a" and "b" in lst:
#     print("yes")
# else:
#     print("no")
# new test
# dic = {"name" : "rachid", "second_name": "lahmaidi"}
# print(dic)
# print(len(dic))
#new test
# if 2 %2 == 0:
#     print("yes")
# #new test
# dic = {"name":"rachid", "second_name": "lahmaidi"}
# for k in dic.keys():
#     print(k)
#new test about strings
# string = "rachid"
# print(string[1])
#new test about not and in
# lst = ["a", "b", "c"]
# if "d" and "f" not in lst:
#     print("yes")
# else:
#     print("no")
class test:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def  test1(self):
        print(self.name)
    def test2(self):
        self.test1()

t = test("rachid", 10)
t.test2()