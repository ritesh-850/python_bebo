#------------------ data that we don't need to change is taken in tuple format

# #----------------------------------creating a tuple:----------------------------------
# mytuple=(10,20,30,40)
# print(mytuple)
#
# #----------------------acessing the elements of tuple:------------------------------------
# mytuple1=(10,20,30,"Parkhi",'Python')
# print(mytuple1)
# print(mytuple1[0])
# print(mytuple1[-1])
# print(mytuple1[3])

# #-------------------------------range of index(slicing):------------------------------------
# mytuple=(10,"Parkhi",20,30,"python")
# print(mytuple[3])
# print(mytuple[1:3])
# print(mytuple[2:5])
# print(mytuple[-4:-1])

# #-------------------------change item value:--------------------------------
# mytuple=(10,20,40,"Parkhi","Python")
# print(mytuple)
# mytuple[1]="Welcome"
# print(mytuple)

# #-------------------------------- reading tuple value using a loop:---------------------------
# mytuple=(10,20,"Parkhi","python",30)
# print(mytuple)
# for i in mytuple:
#     print(i)

# #--------------------------length of tuple:---------------------------
# mytuple=(10,20,30,"Parkhi","python")
# print(len(mytuple))

# # ----------------------adding item in tuple:-------------------------
# mytuple=(10,20,30,"Parkhi","python")
# #mytuple.append("welcome")
# # mytuple.insert(1,"welcome")

# # #--------------------------removing element:----------------------------------
# tuple=(10,20,"Parkhi","python",30,40)
# #tuple.pop()
# # #Method 2:
# del tuple
# print(tuple)
# # #method 3:
# tuple.clear()
# print(tuple)

# # -------------------------method 1: searching of index of element:----------------------------
# mytuple=(10,20,"Parkhi","python",30,40)
# print(mytuple.index("Parkhi"))
# #method 2: total no of occurances:
# print(mytuple.count(40))

# #empty tuple
# tup1=()
# print(tup1)

# #---------------------------updating tuple value by converting it to a list:------------------------
# mytuple=(10,20,"Parkhi",30,"python")
# mytuple=[10,20,"Parkhi",30,"python"]
# print(mytuple)
# mytuple[0]="Welcome"
# print(mytuple)
# mytuple=("welcome",20,"Parkhi",30,"python")
# print(mytuple)

# #-----------------------copy a tuple:-------------------
# #method 1:
# mytuple=(10,20,30,"parkhi","python")
# mytuple1=mytuple.copy()
# print(mytuple1)
# print(mytuple)

# list1 = ['a','b','c']
# list2 = ['i','j','k']
# for i in list1:
#     list2.append(i)
# print(list1)


#----------------------------------------combine two list---------------------------------------------
# list1 = ['a','b','c']
# list2 = ['i','j','k']
# list1.extend(list2)
# print(list1)
#
#
#
#------------------------------------reading a list of no from user inputs----------------------------------------
# a=input().split(",")
# print(a)


# b=tuple(map(int,(input("Enter the number:"))))
# print(b)

# b=list(map(int,(input("Enter the element of list:").split(","))))
# print(b)

# number = list(map(float,(input("Enter the element of list :").split(","))))
# print(number)


#-----------reverse list------------
mylist=[12,9,4,5]
mylist.sort()
print(mylist)

#--------------sorting a list----------------
mylist=[12,9,4,5]
mylist.sort(reverse = True)
print(mylist)

#---------------count a list-----------
mylist=[12,9,4,5,47,58,65,95,14,14,14,14]
print(mylist.count(14))
