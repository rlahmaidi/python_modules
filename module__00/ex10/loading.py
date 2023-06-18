from time import sleep, time
from timeit import timeit
from random import randint
# from math import rand

def timer(listy):
    for element in listy:
        yield element

def ft_progress(listy):
    eta = timeit(stmt= 'ft_progress(listy)', globals=globals(), number= 1000)
    # text = "ETA: " + str(eta) + "[ "
    begin = time()
    i = 0
    flesh = "=>"
    for e in listy:
        text = "ETA: " + "{:.5f}".format(eta) + "s [ "
        percent = (i / len(listy)) * 100
        text += str(percent) + "%]" + " ["
        if randint(0,1000) > 990 :
            flesh = '=' + flesh
        text += flesh + " ] "
        text += str(i) + "/" + str(len(listy))
        inter_time = time() - begin
        text += " | elapsed time " + "{:.5f}".format(inter_time)
        # here i should add flessh
        LINE_CLEAR = '\x1b[2K'
        print(end=LINE_CLEAR)
        print(text, end="\r")
        i += 1
        yield e
    
    # text = "ETA: 8.67s [ 23%][=====> ] 233/1000 | elapsed time 2.33s"






listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)