#10
#Method overloading and Method Overriding (not availiable in python)

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    #Default value is None.. If not given does not give any errors
    def sum(self,a=None,b=None,c=None):

        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a != None and b != None:
            s=a+b
        else:
            s=a

        return s



s1 = Student(58,69)

print(s1.sum(5,9,6))