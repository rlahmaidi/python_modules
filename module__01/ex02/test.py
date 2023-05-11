
from vector import Vector


if __name__ == "__main__":
    # row_vector = Vector([[1, 2, 3, 5]])
    # column_vector = Vector([[1],[2],[4]])
    # row_vector.print_data()
    # column_vector.print_data()
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
    v1 = Vector([[1,2,3.3]])
    v2 = v1/2
    v2.print_data()
