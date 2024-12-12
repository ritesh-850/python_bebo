#constructor name is fixed def __init__(self)
#two constructor are there default constructor and / Parameterized constructor

#
class Myclass:
    def __init__(self):
        print("I am constructor of the class")
    def m1(self):
        print("Hello! I am the method of the class")
obj = Myclass()
obj.m1()

#
class myclass:
    def __init__(self):
        print("I am constructor of the class")
    def m1(self):
        print("Hello! I am the method of the class")
        print(self)  # this will print the object reference
obj = myclass() # this will invoke the constructor automatically
obj.m1() # method we have call explicitly by using object


#----------Parameterized Constructor--------------------
class myclass:
    name="David"   #instance variable
    def __init__(self,name):
        print(name) #Parameterized name
        print(self.name) #instance name
obj=myclass("Abhi")

#
class employee:
    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def display(self):
        print(self.eid,self.ename,self.esal)
obj=employee(102,"David",50000)
obj.display()

#
#__str__() Constructor in python used to define the string representation of an object

class myclass:
    def __str__(self):
        return "Hello I am a method"
obj = myclass()

print(obj)

#
class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"Brand:{self.brand},model:{self.model}"
c=car("Tata","Nexon")
print(c.brand)
print(c.model)
print(c)
del c.brand
#print(c.brand)
del c
#print(c.model)

#



# constructor with loop
class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = []
        for grade in grades:
            if 0 <= grade <= 100:
                self.grades.append(grade)
            else:
                print(f"Invalid grade'{grade}' for {name},skipping.")
    def display(self):
        print(f"Student name: {self.name}")
        print(f"Student garde: {self.grades}")
obj = Student("Abhi",[85,72,65,94,68])
obj.display()



#class: class is a blueprint for creating object
#class created:
class Student:
	name="PArkhi"
#object created:
s1=Student()
print(s1.name)
#Output: PArkhi

object: instance of a class

#class create:
class Car:
	color="Red"
	brand="Honda"
#object create:
c1=Car()
print(c1.color)
print(c1.brand)
#Output:
color=Red
brand=Honda

constructors: _init_(self): execute at the time of object creation

#class create:
class Student:
	name="PArkhi"
	def _init_(self): #default constructor
		print("creating a student database")
#created object:
s1=Student() ->calling constructor

#self: it is a parameter that provide refrence to current instance of class and help us access the variable belonging to that class

#class create:
class Student:
	name="Parkhi"
#constructor created:
	def _init_(self,name,age): #parmetrized constructor
		self.name=name
		self.age=age
		print("adding new record in database")
#object create:
#s1=Student()
#print(s1.name)
#Output: Parkhi

#Attrubute: data stored inside class or object. it is of two types:
#	1. class attribute: same for all object: like name of the college of student
#	2. instanc attribute: different for all objects: like name, roll no of student

#methods: what we can do.
#class is a collection of attribute and methods

#static method: use of decorator "@"
#class Student:
#	@staticmethod
#	def college():
#print("ABC college")

#deleting something in constructor: use of del
#del c #deleting object
#del c.brand