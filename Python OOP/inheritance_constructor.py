#8
#Construction inheritance and MRO(Method resolution order)

# if you create object of sub class it will first try to find init of sub class if not found then it will call init of super class

class A:
    #ConstructorA
    def __init__(self):
        print("in init A")

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")


class B(A):
    # ConstructorB
    def __init__(self):
        super().__init__() #call init A from init B
        print("in init B")

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

a1 = B()

#When B not a child class of A
#MRO left to right---> vid look it will understand
class C(A,B):

    def __init__(self):
        super().__init__()
        print("init C") 