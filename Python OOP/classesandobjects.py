#1
#class and method(function called a method when it is associated with a object)

class Computer:

    def config(self):
        print("i5, 16gb, 1TB")

#x is a also object of int ...
x=9
print(type(x))

#computer object
com1 = Computer()
com2 = Computer()

#com1 is the "self" object that you are passing in the class
Computer.config(com1)
Computer.config(com2)

#Behind the seen com1 goes to ().. com1.config(com1)
com1.config()
com1.config()

#ctrl+click the function---> take you to the method
#BASICALLY SELF IS THE OBJECT THAT YOU ARE PASSING
x.bit_length()