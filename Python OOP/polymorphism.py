#9
# Polymorephism 4 types in python -- > Duck Typing, Operator Overloading, Method Overloading, Method Overridding

class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convent")

class Laptop:

    #here duck typing happens-->
    def code(self,ide):
        ide.execute()

ide =PyCharm()

lap1 = Laptop()
lap1.code(ide)
