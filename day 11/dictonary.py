#dictionary: key :value
#list :mutable
#dictionary is a collection which is ordered. changeable and indexed\
#{'name':'Rana','age':'23'}
#must be unique, must be immutable types
#list and dictionary can have only tuple of keys
#product1:100
#product2:200
#product3:100
# #---how to create a empty dictionary
# mydict={}
# print(mydict)
#---------------with data------------
# mydict={"name":"Rana","age":"23","address":"new york"}
# print(mydict)
#----------------list of tuple for creating dict----------------------
# mydict=dict([("name","Rana"),("age","23"),("address","new york")])
# print(mydict)
#--------------using dict constructor-----------
# mydict=dict(name="Ram",age="23")
# print(mydict)
#accessing the element-------------------------
# mydict={"name":"Rana","age":"23","address":"new york"}
# print(mydict["name"])
# print(mydict["age"])
#print(mydict["deptt"]) #key error

#------------using get() method------------------
# print(mydict.get("name"))
# print(mydict.get("age"))

#modifying dictionary
#--------------adding or update--------------
# mydict={"name":"Rana","age":"23","address":"new york"}
# print(f"before update:{mydict}")
# mydict["age"]=31
# print(f"update value: {mydict}")
# mydict['city']='los angeles'
# print(f"add new pair:{mydict}")

#delete a pair
# del mydict["age"]
# print(f"value after delete: {mydict}")

#pop()
# mydict.pop("age")
# print(f"value after delete: {mydict}")

#using clear
# mydict.clear()
# print(mydict)

#key method
# mydict={"name":"Rana","age":"23","address":"new york"}
# print(mydict.keys())
# #values
# print(mydict.values())
# #items()
# print(mydict.items())


#-----------update-------------
# mydict1={"name":"Rana","age":"23","address":"new york"}
# mydict2={"dept":"govt","city":"los angeles"}
# mydict1.update(mydict2)
# print(mydict1)

#copy() return a copy of dictionary
# mydict1={"name":"Rana","age":"23","address":"new york"}
# mydict2=mydict1.copy()
# print(mydict2)

#fromkeys(): create a copy of dict with a specified keys and a single value
# keys=[1,2,3]
# default_values="Welcome"
# mydict=dict.fromkeys([1,2,3],"Welcome")
# print(mydict)

#setdefault()
# mydict1={"name":"Rana","address":"new york"}
# mydict1.setdefault("age",31)
# print(mydict1)


#itertate using dictionary
# mydict1={"name":"Rana","age":"23","address":"new york"}
# for i in mydict1:
#     print(i)
# for i in mydict1.values():
#     print(i)
# for keys,values in mydict1.items():
#     print(f"{keys}:{values}")

#dictionary comprehension
# square={x:x**2 for x in range(0,11)}
# print(square)

#nested dictionary
# mydict={
#     'person1':{'name':'Ram','age':'23'},
#     'person2':{'name':'abhi','age':'25'}
# }
# print(mydict['person1']['name'])
# print(mydict['person2']['age'])

#merging dictionary
#union operator
#
# mydict1={'a':1,'b':2,'c':3}
# mydict2={'a':1,'c':2}
# merged_dict=mydict1|mydict2
# print(merged_dict)

#COMMON VALUES FROM TWO DICTIONARY
# mydict1={'a':1,'b':2,'c':3}
# mydict2={'a':1,'b':9,'c':5}
# new=set(mydict1.values())
# print(new)
# wow=set(mydict2.values())
# print(wow)
# print(new & wow)

#convert dict key into set
# mydict1={'a':1,'b':2,'c':3}
# a=set(mydict1.keys())
# print(a)

#find unique values from dict
# mydict1={'a':1,'b':2,'c':3,'d':2,'e':5}
# a=set(mydict1.values())
# print(a)

#set of key:value exist in dictionary or not
# mydict1={'A':2,'B':4,'C':5}
# mydict2={'A':10,'B':20}
# a = set(mydict1.items())
# print(a)
# b = set(mydict2.items())
# print(b)
# if mydict1.get('A','B'):
#     print("True")
# else:
#     print("False")

#------write a program to update the dictionary and sum of all values-----
dict1 = {
    'A':89,
    'B':92,
    'C':83
}
print(sum(dict1.values()))

#WAP that convert tuple of number to a list, appends a given number to a list and then convert it back to a tuple
a = (12,25,14,20)
b = list(a)
print(b)
b.append("Abhi")
c=tuple(b)
print(c)

#WAP that removes minimum and maximum value from a set
# A={2,4,5,0,1,9,8}
# list1 = list(A)
# mx,mn=list1[0],list1[0]
# for i in A:
#     if i<mn:
#         mn=i
#     elif i>mx:
#         mx=i
# set1=set(list1)
# set1.remove(mx)
# set1.remove(mn)
# print(set1)

#Return a symmetric difference
set1 = {1,2,3,4}
set2 = {1,5,3}
print (set1 ^ set2)

#from user
# set1 = set(map(int,input("Enter the first elements: ").split(",")))
# set2 = set(map(int,input("Enter the first elements: ").split(",")))
# print(set1 ^ set2)

#Write a python function that finds and returns the index of all occurrences of a specified element in a list using the index method() If the element is not found returns none.
# def find_indices(lst, element):
#     indices = []
#     start = 0
#
#     while start < len(lst):
#         if element in lst[start:]:
#             idx = lst[start:].index(element) + start
#             indices.append(idx)
#             start = idx + 1
#         else:
#             break
#     return indices
# my_list = [1, 5, 3, 3, 4, 6, 5]
# element_to_find = 2
# result = find_indices(my_list, element_to_find)
# print("Indices:", result)

# list1 = [1,2,3,4,2,5]
# ind=[]
# c=int(input("Enter the value"))
# for i in range(len(list1)):
#     if list1[i]==c:
#         #n=list1[i]
#         ind.append(i)
# print("index",ind,"value",c)

#write a python code that find keys in a dictionary that have specified values
dict1 = {
    'A':12,
    'B':10,
    'C':10,
    'D':12,
    'E':10
}
for key,value in dict1.items():
    if value==12:
        print(key)







