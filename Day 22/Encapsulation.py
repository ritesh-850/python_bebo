#Wrapping the data into single module
#consist of getter and setter method


class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    #getter method
    @property
    def name(self):
        return self.__name
    #setter method
    @name.setter
    def name(self,new_name):
        self.__name = new_name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age):
        if new_age>0:
            self.__age=new_age
        else:
            print("Error")
s = Student("Scott",24)
s.name = "Bob"
s.age = 20
print(s.name)
print(s.age)

#
class Product:
    def __init__(self,price,stock):
        self.__price = price
        self.__stock = stock
    #getter method
    @property
    def price(self):
        return self.__price
    #setter method
    @price.setter
    def price(self,new_price):
        if new_price > -1:
            self.__price = new_price
        else:
            print("error")
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self,new_stock):
        if new_stock > -1:
            self.__stock = new_stock
        else:
            print("Error")
P = Product(2000,50)
P.price = -500
print(P.price)
P.stock = -5
print(P.stock)