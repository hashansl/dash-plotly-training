#6

# you can create object of inner class inside the outer class
#OR
# you can create object of inner class outside the outer class provided you use outer class name to call it


class Student:
    #Outer class

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
    #inner Class
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)




s1 = Student('Hashan',2)
s2 = Student('Dananjaya',3)

s1.show()

lap1 = Student.Laptop()
