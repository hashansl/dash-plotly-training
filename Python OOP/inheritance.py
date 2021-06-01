#7

class A:
#Parent/Super Class
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

#inheritance
#single level inheritance
class B(A):
#Child Class/Sub Class
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

#multi level inheritance
class C(B):
    def feature5(self):
        print("Feature 5 is working")



a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.feature1()

c1 = C()
c1.feature1()

#Multiple Inheritance different: when B  is not a child class we can create class C(A,B):