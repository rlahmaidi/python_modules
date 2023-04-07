# import sys

# class test:
#     dic = {"1":1, "2":2, "2": 4}
#     def fun(self,):
#         self.dic["1"] = 6
#         print(self.dic)

# t = test()
# print(t.dic)
# t.fun()
# class test:
#     __count = 0
#     def __hide__(self):
#         print("this is a hidden function")

# t = test()
# # print(t.__count)
class Animal:
  def __init__(self, animalName):
    print(animalName, 'is an animal.')

# Mammal inherits Animal
class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a mammal.')
    super().__init__(mammalName)
    
# CannotFly inherits Mammal
class CannotFly(Mammal):
  def __init__(self, mammalThatCantFly):
    print(mammalThatCantFly, "cannot fly.")
    super().__init__(mammalThatCantFly)

# CannotSwim inherits Mammal
class CannotSwim(Mammal):
  def __init__(self, mammalThatCantSwim):
    print(mammalThatCantSwim, "cannot swim.")
    super().__init__(mammalThatCantSwim)

# Cat inherits CannotSwim and CannotFly
class Cat(CannotSwim, CannotFly):
  def __init__(self):
    print('I am a cat.')
    CannotSwim.__init__('Cat')

# Driver code
cat = Cat()
print('')
bat = CannotSwim('Bat')