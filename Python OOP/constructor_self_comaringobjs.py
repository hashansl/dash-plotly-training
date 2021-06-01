#3

#everytime you crete a object it will get a new space (in heap)
# Size of an object-> depends on number of variables and size of each variable
# who allocated the size to object ? ---> constructor

class Computer:

    def __init__(self):
        self.name = "Navin"
        self.age = 28

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


# object using constructor ()
c1 = Computer()
c2 = Computer()

#compare not a inbuilt function
if c1.compare(c2):
    print("They are same")
