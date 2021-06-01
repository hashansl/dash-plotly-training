#9

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
