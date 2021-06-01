#4

class Car:
    #in here we define class variables (static variables)
    #class varibles affect the all the objects
    #belog to class namespace
    wheels = 4

    def __init__(self):
        #in here we define instance variables
        #instance variables can be change depending on the object
        #belog to instance namespace
        self.mil =10
        self.com ="BMW"

c1 = Car()
c2 = Car()

c1.mil = 8

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

#calling by classname
Car.wheels =5


print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)