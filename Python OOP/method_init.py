
class Computer:

    #Basically we use inti to initialize variables
    def __init__(self):
        print("in init")

    def config(self):
        print("i5, 16gb, 1TB")


#when we creating a object init method will run automatically (for every object it will call once)
com1 = Computer()
com2 = Computer()

com1.config()
com1.config()
