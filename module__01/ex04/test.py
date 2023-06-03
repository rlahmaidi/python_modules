# lst = ["one","two","three", "four", "five", "six"]
# en = enumerate(lst,10)
# for count,element in enumerate(lst):
#     # print(count)
#     print(element)
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]

for  (name, age) in (enumerate(names),enumerate(ages)):
    print( name)
    print(age)

