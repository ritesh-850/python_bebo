# # Task 1
# class Vehicle:
#     brand,model = "Volvo","S60"
#     def display1(self):
#         print(self.brand,self.model)
# class Car(Vehicle):
#     doors = 4
#     def display2(self):
#         print(f"doors:{self.doors}")
# obj = Car()
# obj.display1()
# obj.display2()
#
# #task 2
class Shape:
    def area(self):
        raise NotImplementedError("You have to again use this method")
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l= l
        self.b = b
    def area(self):
        print(self.l * self.b)

class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        print(3.14*self.r*self.r)


shape = [Rectangle(10,20),Circle(10)]
for i in shape:
    i.area()
print()

#
# #Task 3
# class Animal:
#     def __init__(self,sound):
#         self.sound = sound
#     def make_sound(self):
#         print(self.sound)
# class Dog(Animal):
#     def make_sound1(self):
#         print("ABC")
# class Cat(Dog):
#     def make_sound2(self):
#         print("XYZ")
# class Cow(Cat):
#     def make_sound3(self):
#         print("CDE")
# AN = Cow("CDE")
# AN.make_sound3()
# AN.make_sound2()
# AN.make_sound1()

#Task 4
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display1(self):
#         print(f"name:{self.name}--age:{self.age}")
# class Employee(Person):
#     employee_id , salary = 101 , 25000
#     def display2(self):
#         print(f"employee_id:{self.employee_id}--salary:{self.salary}")
# Per = Employee("John",24)
# Per.display2()
# Per.display1()

#Task 5
# class Animal:
#     def make_sound(self):
#         print("Animal Sound")
# class Dog(Animal):
#     def make_sound(self):
#         print("ABC")
# class Cat(Animal):
#     def make_sound(self):
#         print("XYZ")
# class Cow(Animal):
#     def make_sound(self):
#         print("CDE")
#         super().make_sound()
# ans=[Dog(),Cat(),Cow()]
# for i in ans:
#     i.make_sound()

# Task 6
class Appliance:
    def turn_on(self):
        print("Object is turned on")
class Refrigerator(Appliance):
    def turned_on(self):
        print("Refrigerator is turned on")
        # super().turn_on()
class WashingMachine(Appliance):
    def turned_on(self):
        print("Washing machine turned on")
class Microwave(Appliance):
    def turned_on(self):
        print("Microwave turned on")
Appliance=[Refrigerator(),WashingMachine(),Microwave()]
for i in Appliance:
    i.turned_on()

#Task8
class Transport:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")
class Airplane(Transport):
    def move(self):
        print("I am a Airplane")
class Ship(Transport):
    def move(self):
        print("I am a Ship")
class Car(Transport):
    def move(self):
        print("I am a Car")
Transport=[Airplane(),Ship(),Car()]
for transport in Transport:
    transport.move()