#Task 1
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)
obj = Person("David",24)
obj.display()


#Task 2
class Book:
    def __init__(self,name,writer):
        self.name = name
        self.writer = writer
    def __str__(self):
        return f"name:{self.name},writer:{self.writer}"
obj = Book("ABC","XYZ")
print(obj)

#Task 3
class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"Brand:{self.brand},model:{self.model}"
c=car("Tata","Harrier")
print(c.brand,c.model)
del c
print("The object is deleted")

#Task 4
class Student:
    name = "David"
    marks = 94
    def __init__(self,name,marks):
        print(name)
        print(marks)
        self.name = name
        self.marks = marks
obj = Student("Abhi",84)

#task 5
class animal:
    name=""
    def __init__(self,name):
        self.name = name
    def display(self):
        print(self.name)
obj1 = animal("Cat")
obj2 = animal("lion")
obj1.display()
obj2.display()

#Task 6
class shape:
    def __init__(self,type="generic"):
        self.type = type
        print(self.type)
obj = shape("Triangle")
obj = shape()

#Task 7
class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        area = self.l*self.b
        print(area)
obj=rectangle(7,8)
obj.area()

#task 8
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __str__(self):
        return f"name:{self.name},age:{self.age},salary:{self.salary}"
obj = Employee("Abhi",28,56000)
print(obj)


#Task 9
# class BankAccount:
#     def __init__(self,deposit,withdraw,check):
#         print(deposit)
#         print(withdraw)
#         print(check)
#         self.deposit = deposit
#         self.withdraw = withdraw - deposit
#         self.check = check - withdraw
# obj=BankAccount()

class BankAccount:
    def deposit(self,deposit):
        self.deposit = deposit
        print(self.deposit)
    def withdraw(self,withdraw):
        self.withdraw = self.deposit-withdraw
        print(self.withdraw)
    def check(self):
        print(self.withdraw)
obj = BankAccount()
obj.deposit(56000)
obj.withdraw(24000)
obj.check()

#Task 10
# class ShoppingCart:
#     def add(self,add):
#         self.add = add
#         print(self.add)
#     def remove(self,remove):
#         self.remove = self.add-remove
#         print(self.remove)
#     def display_items(self):
#         print(self.remove)
# obj = ShoppingCart()
# obj.add(50)
# obj.remove(15)
# obj.display_items()

# class ShoppingCart:


#Task 11
# class ShoppingCart:
#     total_books = 5
#     def add(self,add):
#         self.add = add
#         print(self.add)
#     def borrow(self,borrow):
#         self.borrow = self.add-borrow
#         print(self.borrow)
#     def display_books(self):
#         print(self.borrow)
# obj = ShoppingCart()
# obj.add(50)
# obj.borrow(15)
# obj.display_books()

#task 12
class Library:
    books=5
    def add(self,add):
        self.books= add + self.books
        print("books added",self.books)

    def borrow(self,borrow):
        self.books=self.books-borrow
        print("books borrow",borrow)

    def display(self):
        print("total books",self.books)

obj=Library()
obj.add(6)
obj.borrow(2)
obj.display()

#task 13
class Circle:
    def area(self,r):
        self.r=r
        print(3.14*self.r*self.r)
    def circumfrence(self,r):
        print(2*3.14*self.r)
obj=Circle()
obj.area(3)
obj.circumfrence(4)