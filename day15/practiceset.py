#task 1
# class greeting:
#     def say_hello(self):
#         print("Hello, Python World")
# obj = greeting()
# obj.say_hello()
from gameenternumber import count


#task 2
# class student:
#     name,grade="Abhi","A+"
#     def display_info(self):
#         print(self.name,self.grade)
# obj = student()
# obj.display_info()

#task 3
# x= 15
# class myclass:
#     y=20
#     def show_variable(self):
#         print(self.y)
#         print(x)
# obj = myclass()
# obj.show_variable()

#task 4
# class library:
#     totalbooks = 0
#     def new_books(self,new):
#         self.totalbooks += new
#         print(self.totalbooks)
# obj = library()
# obj.new_books(5)
# obj.new_books(5)

#task 5
# class car:
#     brand, model = "",""
#     def carInfo(self,brand,model):
#         print(brand,model)
# obj1=car()
# obj2=car()
# obj3=car()
# obj1.carInfo("Hyundai","I20")
# obj2.carInfo("Hyundai","Venue")
# obj3.carInfo("Tata","Nexon")

#task 6
# class calculator:
#     def add(self,a,b):
#         print(a+b)
#     @staticmethod
#     def info():
#         print("This is a calculator class")
# obj = calculator()
# obj.add(5,7)
# calculator.info()

#task 7
# class Employee:
#     name,salary="Abhi",21000
#     def old_salary(self,new):
#         print(self.salary)
#         self.salary += new
#     def new_salary(self):
#         print(self.salary)
# obj=Employee()
# obj.old_salary(25000)
# obj.new_salary()

#task 8
# class Counter:
#     count=0
#     def m1(self):
#         #self.count+=1 #instance variable
#         Counter.count+=1   #static variable/class variables
#         print(self.count)
#         #print(count.count)
# a=Counter()
# a.m1()
# b=Counter()
# b.m1()
# c=Counter()
# c.m1()

#shareable variable/variable is static
# obj1.myfun(40)
# obj1.myfun(30)

# class counter:
#     count = 0
#     def m1(self):

#task9
# class Book:
#     title,author="",""
#     def books(self,title,author):
#         print(title,author)
# obj=Book()
# obj.books("Making India Awesome","Chetan Bhagat")
# obj.books("one indian girl","chetan bhagat")

#task 10
class Rectangle:
    length,width="",""
    def area1(self,length,width):
        area=length*width
        print(area)
obj1=Rectangle()
obj1.area1(10,20)
obj1.area1(10,30)
