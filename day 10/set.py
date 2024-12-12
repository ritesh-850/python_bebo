#
# #set{} it is unordered collection. Doesn't follow the concept of indexing. We can't access element by index like in a list.
# #------------------unordered collection----------------------
# my_set= {1,2,3}
# print(my_set) #the order may vary
#
# #----------------------unique elements---------------------------
# # sets stores unique elements meaning no duplicates are allowed. if you try to add duplicate, they will be automatically ignored
# my_set = {1,2,2,3,4,4}
# print(my_set)
#
# #--------------------mutable--------------
# #change or add the element if the set is created
# my_set = {1,2,3,4}
# my_set.add(5) #add the element
# my_set.remove(2)  #remove the element
# print(my_set)
#
# #---------------------------allowed elements----------------------------
# my_set = {1,'hello',(3,4)}
# print(my_set)
#
# #-----------------------unallowed elements
# # my_set = {1,'hello',2,"Ritesh"}
# # print(my_set)
# #-----------unique elements------------
#
#
#
# #-------------------log creating set
# my_set = {"apple","orange"}
# #accessing the elements from set
# for i in my_set:
#     print(i)
#
# #add items in set
# my_set={"apple","orange"}
# my_set.add("grapes")
# set1 = {"apple","mango","grapes"}
# my_set.update(set1)
# print(set1)
#
# #len()
#
# #remove elements from list
# #method 1: remove()  it gives error
# #method 2: discard() doesn't give error
# my_set={"apple","orange","grapes"}
# my_set.remove("grapes")
# print(my_set)
# set1 = {"apple","mango","grapes"}
# my_set.discard("melon")
# print(set1)
#
# #clear() and delete()
#
# #operation on set
# #union
# set1={1,2,3}
# set2={4,5,6}
# print(set1.union(set2))
#
# #intersection
# set1={"hello","hi"}
# set2={"hello","hi","bye","greetings"}
# print(set1.intersection(set2))
#
#
# #difference
# set1={1,1,2,3}
# set2={3,4,1,5}
# print(set1.difference(set2))
#
# #symetric difference^
# set1={1,2,3,4}
# set2={1,5,2}
# print(set1.symmetric_difference(set2))

#frozenset
# frozenset1=frozenset([1,2,3,4])
# print(frozenset1)
# frozenset1.add(15)
# print(frozenset1)

#list conversion into set--duplicate handling
mylist = [1,2,3,3,4,4]
myset=set(mylist)
print(myset)


