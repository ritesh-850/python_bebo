# it is a set of function that help us to perform a set of instructions. Functions in python are reusable.
# it will take input in form of parameter(argument) and output by using return or print option.
#implicit--> user defined
#explicit--> user defined
# if True:
#     print("Hello")
# else:
#     return

#log 1 declaring the function
# def myfun(): #myfun() is called function
#     print("Hello")
# myfun() #calling the function

#--------parameters/arguments / optional

#log 2
# def myfun(name):  #declaring the function with name:david
#     print("hello",name)
# myfun("David")

#log 3
#def cal(a,b):
#     return(a+b) #not printing but returning some value
#print(cal(10,10))
#
# sum=cal(10,30)
# print(sum)

# log 4
# def fun(i):
#     i=10
# print(fun(10))

#log 5
# def call(a,b):
#     print(a+b)
# call(10,10)
#
# def cal(a,b):
#     return(a+b)
# print(cal(10,20))


#types of functions
#functions doesn't have argument and doesn't return any value
# functions doesn't take argument but return some value
# functions takes argument but no return value
# function takes argument and also return value

#
# def sum(a,b):
#     return a+b
# print(sum(10,20))
#
# def sum(a,b):
#     print(a+b)
# sum(10,10)

#factorial
# def fact(num):
#     factorial = 1
#     for i in range(1, num+1):
#         factorial += i
#         return factorial
# num =5
# print(fact(num))

#global variable , local variable
# they both are different on the basis of scope(How we can access them)
#global variable
# global_var=20
# local variable
# def fun():
#     local_var=10
#     print(local_var) # we cannot directly access them
#
# print(global_var)
#
#
#log 2
# xy = 100
#
# def cool():
#     xy = 200
#     print(xy)
# cool()
# print(xy)
#
# change the value of global variable inside the function
xy = 100
def cool():
    global xy
    xy=500
    print(xy)
#cool()
print(xy)
# this is not mandatory to declare the global variable outside the function. we can also declare them inside the function.
#
#--------------parameters/Arguments----------------
#positional argument
#keyword argument
#default keyword argument
# variable length argument
# keyword only variable-length argument
#
# positional argument
# def fun(i,j):
#     print(i,j)
# fun(10,20)
#
# fun(i=10,j=20) # keyword arguments
#
#log 2
#default value arguments --> keeping the value of the argument fixed i.e given by the user
def fun(i,j=200):
     print(i,j)
fun(10,20)
#fun(100)
#
#
# def greeting(name,greetmsg):
#     print(greetmsg + " " + name)
# #positional argument
# greeting("Abhi","Hello")
# # keyword argument
# greeting(name="Abhi",greetmsg="Hello")
#
#
#
def fun(a,b,c):
     print(a,b,c)
fun(10,20,30)
fun(10,b=20,c=30)
#

fun(10,b=20,30)



# create a function to return the greater of two numbers
# def num(a,b):
#     if a<b:
#         print(a)
#     else:
#         print(b)
# num(10,20)
#
# to calculate the area of rectangle where the default height is 10
# def rect(l,b=10):
#     print(l*b)
# rect(30)
#
#
# def data(name,age,salary,address="chandigarh"):
#     print(name,age,salary,address)
# data(name="Abhi",age="25",salary="25000",address="Mohali")
#
#calculate the final price of items
# def price(price,discount=0):
#     discount = price*discount/200
#     print(discount)
# price(500,80)
#
# #log 7
# def si(p,r=10, t=3):
#     si = (p*r*t)/100
#     print(si)
# si(100)
#
# lamda functions --> the function without name, or one line function
#syntax--> lambda arguments:expression
from functools import reduce
# x = lambda a:a+10
# print(x(5))
#
# x = lambda a,b: a*b
# print(x(6,5))
#
# x = lambda a,b,c: a*b*c
# print(x(5,4,6))
#
# write the normal function which is able to find the even number from the list
#list1 = {10,12,14,16,18,19,21,23}
#def func(x):
#    if x%2==0:
#        print(x)
#evenno = list(filter(func,list1))
#print(evenno)
#
#using lambda function
# evenno = list(filter(lambda x:x%2==0,list1))
# print(evenno)
#
#
#city=['jaipur','kota','chandigarh','delhi','muzaffarnagar']
#def length(city):
#    return len(city)
#sort=sorted(city,key=length,reverse=True)
#rint(sort)
#
# lambda function
#sort=sorted(city,key=lambda x:len(x),reverse=False)
#print(sort)
#
# write a function to calculate the square of number
#no = [1,2,3,4,5]
#sq=list(map(lambda x:x**2,no))
#print(sq)
#
# reduce
#z = reduce(lambda x,y:x+y,[1,2,3,4,5])
#print(z)
#
# lambda function is not suitable for complex problems
#
#zip function
#zip()
# a = [10,20,40,50]
# b = [40,50,80]
#
# subjects=['english','maths','hindi','science']
# marks=[40,50,70,80]
# a=zip(subjects,marks)
# print(a)
# res=list(a)
# #print(type(res))
# print(res)
#
#
#
#
def greet(name):
    print("Hello",name)
    print("How are you")
#python argument
greet("Jack")

def add_numbers(n1,n2):
    result = n1 + n2
    print("the sum is",result)
number1 = 5.4
number2 = 6.7
add_numbers(number1,number2)

marks = [55,84,52,34]
length = len(marks)
print("length is", length)
marks_sum = sum(marks)
print("The total marks you got is",marks_sum)
#
#
#
#
#function find_average(marks)
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks/total_subjects
    return average_marks
#calculate the grade and return it
def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >=60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade
marks = [55,64,75,80,74]
average_marks = find_average_marks(marks)
print("Your average marks is:", average_marks)
grade = compute_grade(average_marks)
print("your grade is:", grade)


#-----args-------positional variable length arguments, allows a func to accept any no of positional arguments
#----kwargs------keyword variable length arguments, which will be passed as a tuple to the function

#-------log-----------
def greet(*name):
    print("Hello",{name})

greet("David")
# greet("David","John","Merry","Bob")

#variable length keyword arguments(**kwargs)
#arguments passed as a key value pair
def student_info(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} : {value}')
student_info(name="Bob",id=102)


#both
def display_info(*args,**kwargs):
    print("positional arguments",args)
    print("Keywords arguments",kwargs)
display_info(1,2,3,name="Abhi",age=30,id=102,city="new york")


#positional argument with variable length
def greet(name,*args):
    print(name,args)
greet("John","David","Bob",30)

#
def greet(name,*args,**kwargs):
    print(name)
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(f"{i},{j}")

greet(300,'Merry','John',25,name1="Bob",age=30)