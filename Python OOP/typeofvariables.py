#4

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
