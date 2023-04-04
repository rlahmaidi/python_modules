import sys

class test:
    dic = {"1":1, "2":2, "2": 4}
    def fun(self,):
        self.dic["1"] = 6
        print(self.dic)

t = test()
print(t.dic)
t.fun()
