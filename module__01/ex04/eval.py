import sys


class Evaluator:
    def __init(self,):
        pass
    def zip_evaluate(self,coefs, words):
        if not isinstance((coefs, words), list):
            print("this function takes two list as a param")
            sys.exit()
        elif len(coefs) != len(words):
            print("the two list should be the same length")
            return -1
        else:
            for coef,word in zip(coefs,words):
                

    
    def enumerate_evaluate(self,coefs, words):