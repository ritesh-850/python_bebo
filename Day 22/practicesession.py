#Task 1
# print("start")
# a,b = 10,0
# try:
#     result = a / b
#     print(result)
# except Exception as e:
#     print(e)

#Task 2
# class Integer(Exception):
#     def __init__(self,msg = "Non-integers are not allowed"):
#         self.msg = msg
#         super().__init__(self.msg)
# def check(num):
#     if num < 0:
#         raise ValueError("Please enter the integer value")
#     else:
#         print(f"The number entered is : {num}")
# try:
#     num1 = int(input("Enter the number: "))
#     num2 = int(input("Enter the number: "))
#     check(num1)
#     check(num2)
# except ValueError as e:
#     print(e)
#
# # Task 3
# list = list(map(int,input("Enter the list").split(",")))
# index = int(input("enter the index:"))
#
# try:
#     a = list[index]
#     print(a)
# except IndexError as b:
#     print(b)


#task 4
# mydict = {"apple":150,"banana":50,"grapes":60}
# name = input("Enter the name: ")
# try:
#     print(mydict[name])
# except KeyError:
#     print(f"{name}")

#Task 5
# num = int(input("Enter the numbers:"))
# try:
#     if num < 0:
#         raise ValueError("Please enter the valid number")
#     else:
#         print(num**2)
# except ValueError as e:
#     print(e)

#Task 7
# class InvalidAgeException(Exception):
#     def __init__(self,msg = "must be less than 18"):
#         self.msg = msg
#         super().__init__(self.msg)
# def age(num):
#     if num > 18:
#         raise InvalidAgeException("Please enter the valid age")
#     else:
#         print(f"the age you entered is : {num}")
# try:
#     num = int(input("Enter the age:"))
#     age(num)
# except InvalidAgeException as a:
#     print(a)

#Task 8
# class InsufficientBalanceException(Exception):
#     def __init__(self,msg = "Your balance is low you can't withdraw"):
#         self.msg = msg
#         super().__init__(self.msg)
# balance = 20000
# withdraw = 0
# def Bank(balance):
#     if withdraw > 20000:
#         raise InsufficientBalanceException ("Please enter the sufficient amount")
#     else:
#         print(f"Your current balance is: {balance - withdraw}")
# try:
#     withdraw = int(input("Please enter the amount : "))
#     Bank(balance)
# except InsufficientBalanceException as b:
#     print(b)


#Task 9
# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the number: "))
#
# try:
#     if num1 / num2:
#         raise ValueError("Please enter valid number")
#     else:
#         print(f"The number is : ")
# except ValueError as b:
#     print(b)
# except Exception as e:
#     print(e)

#Task 10
# print("start")
# a,b = 10,5
# try:
#     result = a / b
#     print(result)
# except Exception as e:
#     print(e)
# print("Execution Completed of the existing program")




