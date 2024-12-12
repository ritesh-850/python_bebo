#Task 1
# name = input("Enter your name: ")
# def user_name():
#     print("Welcome!",name)
# user_name()

#Task 2
# a = int(input("Enter the number:"))
# b = int(input("Enter the 2nd no:"))
# def calculate():
#     s=a+b
#     print(s)
#     return a
# calculate()

# Task 3
# n = int(input("Enter the number"))
# def cal():
#     if n%2==0:
#         print("Number is even")
#     else:
#         print("number is  not even")
# cal()

#task 4
# a = int(input("Enter the length"))
# b = int(input("Enter the breadth"))
# def area_rect():
#     area = a * b
#     print(area)
#     return area
# area_rect()

# Task 5
# n = int(input("Enter the number:"))
# def stars():
#     for i in range(n):
#         for j in range(i+1):
#             print("*",end="")
#         print()
# stars()

#Task 6
# a = int(input("Enter the 1st no:"))
# b = int(input("Enter the 2nd no:"))
# c = int(input("Enter the 3rd no:"))
# def demonstrate(c=10):
#     print(a,b,c)
# demonstrate()

#task 7
# n = int(input("Enter the number:"))
# def palin():
#     n = int(input("Enter the number:"))
#
#     temp = n
#     sum = 0
#     while n>0:
#         r =n%10
#         sum = sum*10+r
#         n = n//10
#     if temp==sum:
#         print("Palindrome no")
#     else:
#         print("not palindrome")
# palin()

#task 8
# def fibonacci():
#     n=int(input("Enter the number:"))
#     n1=0
#     n2=1
#     for i in range(n):
#         print(n1,end="")
#         n1,n2=n2,n1+n2
# fibonacci()
# n = int(input("Enter the number:"))
# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(n))

#task 9
# n = int(input("Enter the number:"))
# def cal(n):
#     if (n==0):
#         return 0
#     return cal(n-1)+n
# sum = cal(n)
# print(sum)

#task 10
# no = [2,4,8]
# sq=list(map(lambda x:x**2,no))
# print(sq)

#task 11
# list1 = {10,15,13,18,19,17,23}
# even = list(filter(lambda x:x%2==0, list1))
# print(even)


#task 12
# no = [1,2,3]
# s = list(map(lambda x:x+x,no))
# print(s)

#task 13
# def total(x,y):
#     return x+y
# n=int(input("Enter 1st number:"))
# o=int(input("Enter 2st number:"))
# print(total(n,o))
# def fun_in_fun(total,y ):
#     return
# fun_in_fun(2,3)

# #task 15
# no = [2,3,4]
# s = list(map(lambda x:x*x,no))
# print(s)

# task 14
# xy = 5
# def g_var():
#     x=10
#     print(x)
#     def var():
#         y = 20
#         print(y)
#         print(x)
#     var()
# g_var()
# print(xy)

#task 17
#def find_average_marks(marks):
#     sum_of_marks = sum(marks)
#     total_subjects = len(marks)
#     average_marks = sum_of_marks/total_subjects
#     return average_marks
#
# def compute_grade(average_marks):
#     if average_marks >= 80:
#         grade = 'A'
#     elif average_marks >=60:
#         grade = 'B'
#     elif average_marks >= 50:
#         grade = 'C'
#     else:
#         grade = 'F'
#     return grade
# marks = [55,64,75,80,74]
# average_marks = find_average_marks(marks)
# print("Your average marks is:", average_marks)
# grade = compute_grade(average_marks)
# print("your grade is:", grade)

#task 16
# list1 = [0,1,4,7,8,9]
# def min_max(list1):
#     mn=mx=list1[0]
#     for i in list1:
#         if i<mn:
#             mn=i
#             print("Minimum number is:")
#         elif i>mx:
#             mx=i
#             print("Maximum number is:")
#     res = (mn,mx)
#     return res
# print(min_max(list1))

#task 18
def frequency(*args,**kwargs):

    

