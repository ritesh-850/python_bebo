#  Calculate the difference in days between two dates: 15th august 2025 abd 1st January 2025?
import datetime

date1 = datetime.date(2025,8,15)
date2 = datetime.date(2025,1,1)
date_differnce = date1-date2
print(date_differnce)

# Write a counter class with class variable count to keep track of how many objects have been created. Test this by creating multiple objects and printing the count?
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
obj = Counter()
obj1 = Counter()
obj2 = Counter()
print("How many objects Created", Counter.count)

#Write a program to print the current date and time in the format YYY-MM-DD HH:MM:SS. Create a datetime object for 1st K=January 2025, 12:00PM and print it in the format Day-Month, Year
# at HH:MM?
date = datetime.date(2025,1,1)
print(f"{date.day}-{date.month},{date.year}")
time = datetime.time(12,0,0)
print(f"{time.hour}:{time.minute}")

#Write a Product class with instance attributes for name and price. Add a class method set_discount (cls,discount) to apply a discount to all products. Use this class method to change the
# price of all created products?
# class Product:
#     discount = 0
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     @staticmethod
#     def set_discount(items,discount):
#         return items*(1-discount/100)
#     def display(self):
#         print(f"Name of the product:{self.name}and price of the product:{self.price}")
# obj = Product("daal",100)
# less_price = product.discount()

#Create a class Car with:
# • An instance variable brand
# • A class variable wheels initialised to 4
# • Add a method show() to print both the variables
class Car:
    wheel = 4
    def __init__(self,brand):
        self.brand = brand
    def show(self):
        print(f"Brand is:{self.brand}and wheel is:{Car.wheel}")
obj4 = Car("Skoda")
obj4.show()
obj3 = Car("Apollo")
obj3.show()

# Write a program to add 30 days to the current date and print the result?
today = datetime.date.today()
future_day = today + datetime.timedelta(days = 30)
print(future_day)

# Extend the Car class to include a method delete_attribute(attr_name) that checks if the attribute exists before deleting it. Print an appropriate message if the attribute does not exist?
class Car:
    def __init__(self,brand,name):
        self.brand = brand
        self.name = name
    def display(self):
        print(f"brand:{self.brand} name:{self.name}")
    def delete_attribute(self):
        print("Attribute is deleted")
obj5 = Car("Skoda","Laura")
obj5.display()
del obj5.brand
# print(obj5.brand)
obj5.delete_attribute()

#Create a class book with constructor that initializes the title. Override the del method to print a message when object is deleted. Create and delete a Book object to demonstrate this?
class Book:
    def __init__(self,title):
        self.title = title
    def display1(self):
        print(f"Object exist : {self.title}")
    def display(self):
        print("Object is deleted")
obj6 = Book("Self Creation")
obj6.display1()
del obj6.title
obj6.display()

#Create a class Product with:
# • A constructor that takes name and price.
# • A class method from_discounted_price(name,discounted_price,discount_percentage) that
# initialize a product based on discounted price.
# • Demonstrate the use of both constructors.
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def update(self,Q_change): #updating the quantity
        self.quantity+=Q_change #previous+new=final quantity
    def value(self):
        return self.price*self.quantity #quantity*price =Formula of finding total value(for all item)
    def display(self):
        print(f"Name of the item is: {self.name} and quantity of the item is: {self.quantity}")
obj7=Product("ABC",1500,2)
obj7.value()
obj7.display()
obj8=Product("PQR",2500,4)
obj8.display()
obj8.value()