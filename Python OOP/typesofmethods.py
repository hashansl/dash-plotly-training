#5

#3 types of methods
#Instance methods
#Class methods
#Static methods

class Student():

    #defining static variable outside constructor
    school ="GSC"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    #instance method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    #Incetance methods has two types
    #Accessor methods--> Only fetching the value
    #Mutator methods --> Modify the value

    #accessor
    def get_m1(self):
        return self.m1
    #mutator
    def set_m1(self, value):
        self.m1 = value

    #if your are working with instance(obj) use self
    #if you are working with class use cls

    #use decorator to pass class to ()
    @classmethod
    def getSchool(cls):
        return cls.school

    #keep it empty ()
    #static method-no class/no object connection
    @staticmethod
    def info():
        print("This is abc")



s1 = Student(34,67,32)
s2 = Student(89,32,162)

print(s1.avg())
print(Student.getSchool())
print(Student.info())