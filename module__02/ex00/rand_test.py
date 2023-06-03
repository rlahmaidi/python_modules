#Abstract Base Classes for Containers¶
from collections.abc import Iterable

# Return double of n
# def addition(n,m):
#     return n + m
 
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# numbers1 = (10,20,30,40)
# # result = map(addition, numbers, numbers1)
# # print(result)
# # print(list(result))
# print(type(n for n in numbers))


# #Define a function to check if a number is a multiple of 3
# def is_multiple_of_3(num):
#     return num % 3 == 0
 
# # Create a list of numbers to filter
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# # Use filter and a lambda function to filter the list of numbers
# # and only keep the ones that are multiples of 3
# result = list(filter(is_multiple_of_3, numbers))
 
# # Print the result
# print(result)  # [3, 6, 9]

# python code to demonstrate working of reduce()
 
# importing functools for reduce()
# from  functools import reduce
 
# # initializing list
# lis = [1]
 
# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(reduce(lambda a,b: a *b, lis))
# lst = [1,2]
# if isinstance(lst, Iterable):
#     print("yes")
