class second_class:
    def __init__(self,number, name = "rachid"):
        self.number = number
        self.name = name

class first_class:
    def __init__(self,integer = 0):
        self.integer = integer
    def __mul__(self, other):
        return self.integer * other.number


if __name__ == "__main__":
    first = first_class(1)
    second = second_class(3, "lahmaidi")
    print("the product is ", second * first)
        