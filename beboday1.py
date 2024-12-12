#log 1
#a=10
#b=90.2
#c="asf"
#print(type(a),type(b),type(c))

#log 2
#a=10
#b=20.5
#c="welcome"
#print(a,b,c)

#log 3
#a=100
#b=100
#c=100
#a=b=c = 100
#print(a,b,c)

#log 4
#x=10
#y=20
#print("before swapping the numbers")
#print(x,y)
#y, x=x,y
#print("After swapping the numbers")
#print(x,y)

#log 3
#a=10
#b=20
#print(a)
#print(b)
#del a #delete the variable a from memory
#print(a)
#print(b)


#log 4 Operators
# a=5
# b=2
# print(a+b)
# print(a-b)
# print(a/b)
# print(a//b)
# print(a*b)
# print(a**b)

# program of simple interest
# P=100
# R=2
# T=5
# si=(P*R*T)/100
# print(si)
#
# # Area of circle
# R=3
# ar = 3.14* R**2
# print(ar)

# import math
# radius = float(input("enter radius =70"))
# ar = math.pi * radius**2
# print(ar)

# relational operators
# a=5
# b=6
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)
# print(a<=b)
# print(a>=b)

#Logical operators
# a=True
# b=False
# print(a and b)
# print(a or b)
# print(not b)

# lists
# x=[1,2,3,4,5]
# y=x #it use references
# z=[1,2,3,4,5] #it is a separate list
# print(x is y) # "is" operator will compare references
# print(x is z) #
# print(x is not y)
# print(x is not z)

# Concatenation
# print("hello" + "world")
#
# # log 5
# name,age,sal = "ganja",25,1000
# print("Name is",name)
# print("Age is",age)
# print("Sal is",sal)
# print("Name is : %s , Age is : %d , Sal is : %f "%(name,age,sal))
# print("Name is :{} , Age is :{} , Sal is :{}" .format(name,age,sal))

#log 6
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = a%b
print("Sum of a and b is:",c)
