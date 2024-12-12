#Task 1
# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         print(f"make:{self.make},model:{self.model},year:{self.year}")
#
#     def start_engine(self):
#         print("Engine is starting")
# obj1 = Car("Tata","Harrier",2019)
# obj1.start_engine()
#
# obj2 = Car("Hyundai","Creta",2020)
#
# obj3 = Car("MG","Hector",2022)

#Task 2
# class Company:
#     company_name = "BEBOTECH"
#     def __init__(self,employee_name,designation):
#         self.employee_name=employee_name
#         self.designation=designation
#     def display(self):
#         print(f"employee_name:{self.employee_name},designation:{self.designation},Company is:{Company.company_name}")
# obj1 = Company("David","Tester")
# obj1.display()
#
# obj2 = Company("John","Developer")
# obj2.display()

#Task 3
# class Counter:
#     count = 0
#     def __init__(self):
#         Counter.count += 1
# obj1 = Counter()
# obj2 = Counter()
# print(f"Total Object created:", Counter.count)

#Task 4
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"name:{self.name},age:{self.age}")
# obj = Person("David",25)
# obj.display()
# obj2 = Person("Rahul",27)
# obj2.display()

#Task 5
# class Person:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def specification(self):
#         print(f"brand:{self.brand},model:{self.model}")
# obj1=Person("HP","Pavilion")
# obj1.specification()
#
# obj2=Person("Dell","Inspiron")
# obj2.specification()

#Task 6
# import math
# class Point:
#     def __init__(self,x1,x2,y1,y2):
#         self.x1 = x1
#         self.x2 = x2
#         self.y1 = y1
#         self.y2 = y2
#     def calculate(self):
#         res = math.sqrt(((self.x2-self.x1)**2)+((self.y2-self.y1)**2))
#
#         print(res)
# obj = Point(3,4,7,1)
# obj.calculate()

#Task 7
# class Employee:
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#     def give_raise(self,percent):
#         self.percent = self.salary + 15000
#         print(f"id:{self.id},name:{self.name},salary:{self.salary}")
#         print("New Salary is")
#         print(self.percent)
#
# obj = Employee(101,"David",8000)
# obj.give_raise(2)


#Task 8
# class product:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def





