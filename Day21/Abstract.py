#hidding the implementation details
#classes that cannot be initiated on their own and are meant to be sub classed.
#they serve as a bluprint
#classes that have abstract method which don't have bodies
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#             pass
#key component: abc.ABC,  abc.abstractmethod,    abc.abstractproperty

from abc import ABC, abstractmethod
# class A(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
# class B(A):
#     def m2(self):
#         print("class B")
#     def m1(self):
#         print("class A")
#     @abstractmethod
#     def name(self):
#         pass
# class C(B):
#     def m3(self):
#         print("class C")
#     def name(self):
#         print("method of class B")
# obj = C()
# obj.name()
# obj.m3()
# obj.m2()
# obj.m1()

#method overriding with abstract

class Shape(ABC):
    def __init__(self,w,h):
        self.w = w
        self.h = h
        print(self.w,self.h)
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def area(self):
        print(f"{self.w * self.h}")
    def perimeter(self):
        print(2*self.w+self.h)
obj = Rectangle(2,5)
obj.area()
obj.perimeter()


