import numpy as np
import sys
import random


class NumPyCreator:
    def from_list(self, lst):
        return np.array(lst)

    def from_tuple(self, tpl):
        return np.array(tpl)

    def from_iterable(self, itr):
        lst = []
        for element in itr:
            lst.append(element)
        return np.array(lst)


    def from_shape(self, shape, value=0):
        if not isinstance(shape, tuple) or len(shape) != 2:
            print("the first argument should be a tuple that \
                  define the shape of the array")
            sys.exit()
        lst = [value] * (shape[0] * shape[1])
        return np.array(lst).reshape(shape)

    def random(self, shape):
        if not isinstance(shape, tuple) or len(shape) != 2:
            print("the first argument should be a tuple (,) that \
                  define the shape of the array")
            sys.exit()
        lst = []
        for i in range(0,shape[0] * shape[1]):
            lst.append(random.randint(0,100))
        return np.array(lst).reshape(shape)

    def identity(self, n):
        columns = []
        for i in range(n):
            line = [0] * n
            line[i] = 1
            columns.append(line)
        return np.array(columns).reshape(n,n)

