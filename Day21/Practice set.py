#Task 1
class A:
    def show(self):
        print("it is class A")
class B(A):
    def show1(self):
        print("It is class B")
print(issubclass(A,B))
print(issubclass(B,A))
# obj = B()
# obj.show1()
# obj.show()

#
class Person:
    def display1(self):
        print("I am person class")
class Employee(Person):
    def display2(self):
        print("I am class Employee")
obj1 = Employee()
obj1.display1()
obj1.display2()

#
class Shape:
    def __init__(self,l,b,r):
        self.l = l
        self.b = b
        self.r = r
class Rectangle(Shape):
    def area1(self):
        print({self.l*self.b})
class Circle(Rectangle):
    def area2(self):
        print(3.14*self.r*self.r)
obj = Circle(2,5,4)
obj.area1()
obj.area2()

#
class Parent:
    def __init__(self):
        print("Parent class")
class Child(Parent):
    def display(self):
        print("Child")

obj2 = Child()
obj2.display()

#task 7
class Vehicle:
    def display(self):
        print("I am Vehicle")
class Car(Vehicle):
    def display1(self):
        print("I am car")
class Bike(Car):
    def display2(self):
        print("In am Bike")
obj3 = Bike()
obj3.display2()
obj3.display()
obj3.display1()

#
class A:
    def show(self):
        print("it is class A")
class B(A):
    def show(self):
        print("It is class B")
obj = B()
print(isinstance(obj,B))

#task 6
class Specifier:
    def public(self):
        print("I am public class")

    def __Private(self):
        print("I am private method")

    def _Protected(self):
        print("I am protected")
class Base(Specifier):
    def display(self):
        print(self._Protected)
obj4 = Base()
obj4.display()
obj4.public()
#obj4.__Private()

#print(obj4.Public__Private_method)
#print(obj4._Protected_method)

#Task 9
class BankAccount:
    def __init__(self,ac_no,balance):
        self.__ac_no = ac_no
        self.__balance = balance
    def deposit(self,deposit):
        self.deposit = deposit + self.__balance
        print(self.deposit)
    def withdraw(self,withdraw):
        self.deposit = self.__balance - withdraw
        print(self.withdraw)
obj = BankAccount(1011,500)
obj.deposit(100)
obj.withdraw(20)


#Task 10
# from abc import ABC
# class A(ABC):
#     @staticmethod
#     def show(self):
#         pass
# class C(A):
#     def display(self):
#         print("class C")
#     def show(self):
#         print("class A")
# obj = A()
# obj.show()






