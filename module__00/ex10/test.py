from tqdm import tqdm
import time
from time import sleep
import timeit
 
 
# for i in tqdm (range (101),
#                desc="Loading…",
#                ascii=False, ncols=75):
#     time.sleep(0.01)
     
# print("Complete.")
# def timer(listy):
#     begin = time()
#     for element in listy:
#        sleep(100000000000000000000000000)
#        yield element

# n = 5
# result = timeit.timeit(stmt='timer(range(1000000))', globals=globals(), number=n)
# print("the execution time is {: .9f}".format(result))
# print(result / 5)

# import time

# chars = 'ABCDEFGH'
# loop = range(1, len(chars) + 1)

# for idx in loop:
#     print(chars[:idx],end = "\r")
#     time.sleep(.5)
import time

chars = 'ABCDEF'
loop = range(1, len(chars) + 1)

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

for idx in reversed(loop):
    print(chars[:idx])
    time.sleep(.5)
    print(LINE_UP, end=LINE_CLEAR)


