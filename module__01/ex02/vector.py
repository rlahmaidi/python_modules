import sys

class Vector:
    def __init__(self,values=[[]]):
        self.values = values
        self.shape =(len(self.values), len(self.values[0]))
    def __init__(self, number):
        self.values = []
        for i in range(0, number):
            self.values.append([i/1.0])
        self.shape =(len(self.values), len(self.values[0]))
    def __init__(self,range_beg, rang_end):
        if range_beg > rang_end:
            print("the first number should be the smallest!!!")
            sys.exit()
        else:
            self.values = []
            for i in range(range_beg, rang_end):
                self.values.append([i/1.0])
            self.shape =(len(self.values), len(self.values[0]))
    def dot(self,vector):
        summ = 0
        if not isinstance(vector, Vector):
            print("please provide a proper vector")
        elif vector.shape != self.shape:
            print(". product can only done between 2 vectors of the same shape")
        elif self.shape[0] == 1:
            # summ = [self.values[x] + vector.values[x] for x in range(0,len(self.values))]
            for i in range(len(self.values[0])):
                summ += self.values[0][i] * vector.values[0][i]
        else:
            for i in range(len(self.values)):
                summ += self.values[i][0] * vector.values[i][0]
        print("the . product is: ", summ)
    
    def T(self):
        if self.shape[0] != 1:
            lst = [[self.values[x][0] for x in range(len(self.values))]]
        else:
            lst = [[self.values[0][x]] for x in range(len(self.values[0]))]
        print(lst)
    def __add__(self, other):
        if not isinstance(other, Vector):
            print("please provide a 2 proper Vector")
            sys.exit()
        elif other.shape != self.shape:
            print("summ can only done between 2 vectors of the same shape")
        elif self.shape[0] == 1:
            lst = []
            for i in range(len(self.values[0])):
                lst.append(self.values[0][i] + other.values[0][i])
            result = Vector([lst])
            return result
        else:
            lst = []
            for i in range(len(self.values)):
                lst.append([[self.values[i][0] + other.values[i][0]]])
            result = Vector(lst)
            return result

    def __mul__(self,scaler):
        if not isinstance(scaler, (int, float)):
            print("multiplication can only be between an integer and a vector")
            sys.exit()
        elif self.shape[0] == 1:
            lst = []
            for i in range(len(self.values[0])):
                lst.append(self.values[0][i] * scaler)
            return Vector([lst])
        else:
            lst = []
            for i in range(len(self.values)):
                lst.append([self.values[i][0] * scaler])
            return(Vector(lst))

    def __rmul__(self,scaler):
        if not isinstance(scaler, (int, float)):
            print("multiplication can only be between an integer and a vector")
            sys.exit()
        elif self.shape[0] == 1:
            lst = []
            for i in range(len(self.values[0])):
                lst.append(self.values[0][i] * scaler)
            return Vector([lst])
        else:
            lst = []
            for i in range(len(self.values)):
                lst.append([self.values[i][0] * scaler])
            return(Vector(lst))
    def __truediv__(self, sclar):
        if not isinstance(sclar, (float, int)):
            print("vetcors can only be devided by floats")
            sys.exit()
        if self.shape[0] == 1:
            lst = []
            print("we are in row vector")
            for i in range(len(self.values[0])):
                lst.append(self.values[0][i] / sclar)
            return(Vector([lst]))
        else:
            lst = []
            for i in range(len(self.values)):
                lst.append([self.values[i][0] / sclar])
            return(Vector(lst))
    
    def __rtruediv__(self, scalar):
        raise NotImplementedError("NotImplementedError: Division of a scalar by a Vector is not defined here.")


    def print_data(self):
        print("the values argument: ", self.values)
        print("the shape is : ", self.shape)

# __str__ and ___rpr__ should be implemented


if __name__ == "__main__":
    #       constructors 
    # row_vector = Vector([[1, 2, 3, 5]])
    # column_vector = Vector([[1],[2],[4]])
    # row_vector.print_data()
    # column_vector.print_data()
    v1 = Vector(4,2)
    v1.print_data()
    # #the dot product of row vector
    # first_vector = Vector([[1, 2, 3]])
    # second_vector = Vector([[4, 5, 6]])
    # first_vector.dot(second_vector)
    # #the dot product of column vector
    # first_vector = Vector([[1], [2], [5]])
    # second_vector = Vector([[1],[2],[4]])
    # first_vector.dot(second_vector)
    # #the Transpose vector
    # first_vector = Vector([[1], [2], [5]])
    # second_vector = Vector([[4, 5, 6]])
    # print("the Transpose of first vector is: ")
    # first_vector.T()
    # print("the Transpose of second vector is: ")
    # second_vector.T()
    #       ADD
    #  + column vector
    # first_vector = Vector([[1], [2], [5]])
    # second_vector = Vector([[1],[2],[4]])
    # result = first_vector + second_vector
    # result.print_data()
    # # + row vector
    # print("************** row vector tests*********")
    # v1 = Vector([[1,2,3]])
    # v2 = Vector([[1,3,5]])
    # v3 =  v1 + v2
    # v3.print_data()

    #       __mul__ 
    #     # row vector
    # v1 = Vector([[1,2,4,5]])
    # v2 = v1 * 2
    # v2.print_data()
    #     # culumn vector
    # v1 = Vector([[1],[2],[3],[4.4]])
    # v2 =  v1 * 2
    # v2.print_data()
    # #  rmul 
    # # row vector
    # v1 = Vector([[1,2,4,5.5]])
    # v2 = 3.2 * v1
    # v2.print_data()
    #       truedev
    # row vector
    # v1 = Vector([[1,2,3.3]])
    # v2 = 2.0/v1
    # v2.print_data()
