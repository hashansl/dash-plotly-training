#2
class Computer:

    #Basically we use inti to initialize variables
    #We are actually passing 3 arguments here (com1,cpu,ram) ---> com1 passes automatically
    def __init__(self,cpu,ram):
        self.cpu = cpu;
        self.ram= ram;

    def config(self):
        print("Config is ",self.cpu,self.ram)


#when we creating a object init method will run automatically (for every object it will call once)
com1 = Computer('i5',16)
com2 = Computer('Ryzen 3',8)

com1.config()
com2.config()
