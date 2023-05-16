import sys


class Evaluator:
    def __init(self):
        pass

    @staticmethod
    def zip_evaluate(coefs, words):
        sum = 0
        if not (isinstance(coefs, list) and isinstance(words, list)):
            print("this function takes two list as a param")
            return -1
        elif len(coefs) != len(words):
            print("the two list should be the same length")
            return -1
        elif not all(isinstance(n, (int, float)) for n in coefs):
            print("the coefecient should all be scalars")
            return -1
        else:
            for coef, word in zip(coefs, words):
                sum += len(word) * coef
        return(sum)

    @staticmethod
    def fun(coefs):
        for count, coef in enumerate(coefs):
            yield coef

    @staticmethod
    def enumerate_evaluate(coefs, words):
        sum = 0
        if not (isinstance(coefs, list) and isinstance(words, list)):
            print("this function takes two list as a param")
            return -1
        elif len(coefs) != len(words):
            print("the two list should be the same length")
            return -1
        elif not all(isinstance(n, (float, int)) for n in coefs):
            print("the coefecient should all be scalars")
            return -1
        else:
            it = Evaluator.fun(coefs)
            for count, word in enumerate(words):
                # it = Evaluator.fun(coefs)
                # the above is not correct because
                # each time you get an iterator on the begining
                sum += len(word) * next(it)
        return sum

# words = ["lsii","lsa"]
# coefs = [0.5,1]
# print(Evaluator.zip_evaluate(coefs,words))
# print(Evaluator.enumerate_evaluate(coefs, words))
