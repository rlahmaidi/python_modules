class GenericClass():
    pass

obj1 = GenericClass()

setattr(obj1, 'salary', 100)
setattr(obj1, 'age', 30)
obj1.name = "chi"

print(obj1.salary)  
print(getattr(obj1, 'age'))
print(obj1.name)