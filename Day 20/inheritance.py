#Reusability
#Aquiring all the attributes & behaviour from one class to another class is called inheritance
#class A ---> a,b,c m1() m2()---> A is the parent of class B  (Base class/super class)
#class B --->x,y,z m3() ---->B is a child of class A  (sub class/Derived class)
#code reusability
# Avoid duplicacy

#Example 1 (Single Inheritance)
# class A:  #parent,Base,super
#     def __init__(self):
#         print("I am Constructor")
#     def m1(self):
#         print("Hi I am method from class A")
# class B(A):
#     def __init__(self):
#         print("I am constructor from B")
#     def m2(self):
#         print("Hi I am method from B")
# obj = B()
# obj.m2()
# obj.m1()

#single  [P]-------[C]
#multi level [C1]-------[c2]---------[C3]---------[C4]
#multiple [P1]----->[C]<-----[P2]
#hierarchy [P1]----->[C1]
#           [C2]

# Single using variable
# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b = 100,200
#     def m2(self):
#         print(self.a+self.b)
# obj1 = B()
# obj1.m1()
# obj1.m2()
#
#
# #Multi-level Inheritance
# class A:
#     x,y = 10,20
#     def __init__(self):
#         print("I am constructor of A")
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b = 100,200
#     def __init__(self):
#         print("I am constructor of B")
#     def m2(self):
#         print(self.a+self.b)
# class C(B):
#     i,j = 50,40
#     def __init__(self):
#         print("I am constructor of C")
#     def m3(self):
#         print(self.i+self.j)
# obj2 = C()
# obj2.m1()
# obj2.m2()
# obj2.m3()

#hierarchy inheritance
# class A:
#     def __init__(self):
#         print("I am Parent class")
#     def m1(self):
#         print("class A")
# class B(A):
#     def __init__(self):
#        print("I am constructor B")
#     def m2(self):
#         print("class B")
#
# class C(B):
#     a,b = 10,20
#     def __init__(self):
#         print("I am Base class C")
#     def m3(self):
#         print(self.i + self.j)
# obj = C()
# obj.m2()
# obj.m3()

#mutiple
class A:
    def print1(self):
        print("class A")
class B:
    x,y = 100,200
    def __init__(self):
        print("Class B")
    def print(self):
        print(self.x)
class C(A,B):
    a,b = 10,20
    def print(self):
        print("class C")
    def m1(self):
        print(self.a)

obj1 = C()
obj1.print1()
obj1.print()
obj1.m1()


# Method Overriding
#providing the new body
class A:
    def m1(self):
        print("Class A")
class B(A):
    def m1(self):
        print("class B")
        super().m1()  # invoke immediate class Method
    def print(self):
        print("Hi All")
obj = B()
obj.m1()
obj.print()

#
class A:
    name = "Scott"
class B(A):
    name = "john"
    def test(self):
        print(super().name)
obj = B()
print(obj.name)
obj.test()

# How to access the parent class variables
# class A:
#     a,b = 10,20
# class B(A):
#     x,j = 100,200
#     def m1(self,x,y):
#         print(x+y)
#         print(self.x+self.y)
#         print(self.a + self.b)
#         print(globals().[a] + globals().[b])
# obj2 = B
# obj2.m1()

#method Overloading (not completely supported in python)
#in overloading it matches the arguments and parameters
class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("hello" + name)
        else:
            print("Hello")
obj = Human()
obj.sayhello()
obj.sayhello("John")

#
class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
cal = Calculation()
cal.add()
cal.add(10,20)
cal.add(10,20,30)