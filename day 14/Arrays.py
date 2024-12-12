# its  a collection og similar data types. (Homogeneous collection). In python array is a module. if we want work we have to import the arrays (import array)
#array.array(typecode[elements])

import array
from array import typecodes

# arr = array.array(typecodes,[elements])

#types of typecode
#i-----signed integer(+ve or -ve value)
#I-----unsigned integer(+ve value)
#f----- floating point
#d----- double precession point

#another module numpy,

#creating an array
import array
arr = array.array('i',[1,2,3,4,4,5,5])
print(arr[0])

#accessing the element
print(arr[2])
#modifying the element
arr[1]=6
print(arr)
#adding element in array
arr.append(7)
print(arr)
#Removing the element
arr.remove(3)
print(arr)

# arr.pop(4)
# print(arr)

# arr.clear(2)
# print(arr)

#accessing the last elements
print(arr[-1])

#extend()
arr.extend([7,4])
print(arr)

#insert element at any index
arr.insert(2,20)
print(arr)

#
arr.pop()
print(arr)

arr.pop(2)
print(arr)

#Slicing
#slicing from index
print(arr[1:3])
print(arr[::2])
print(arr[::-1])

# Returns the first occurrence
arr.index(4)
print(arr)

#buffer info: Return a tuple containing memory address and the length of an array
print(arr.buffer_info())


#task 2
#find the sum of elements in an array
#Rotate an array by n position
import numpy as np
# arr = array.array('i',[1,2,3,4,5,6])
# n = int(input("Enter the number"))
# arr=arr[n:]+arr[:n]
# print(arr)


#remove the duplicate element
arr = array.array('i',[1,2,3,4,4,5,6])
i = 0
while(i<len(arr)):
    j = i+1
    while(j<len(arr)):
        if arr[i]==arr[j]:
            arr.pop(j)
        else:
            j+=1
    i+=1
print(arr)

#reverse an array
arr = array.array('i',[1,2,3,4,5,6])
print(arr[::-1])

#sm of an elements
arr = array.array('i',[1,2,3,4,5,6])
