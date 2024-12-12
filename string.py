# a = 'ritesh'
# a1 = "ritesh"
# a2 = str("ritesh")
#
# #why strings are immutable
# it will not change the location it will change the reference
#
#
#
#
# name="Ritesh"
# name(0)="kumar"
# print(name)
#
# message="Welcome"
# print(id(message))
#
# message=message+"to python"
# print(id(message))

#concatenation
str="welcome"
print(str+ "to python")

#print string multiple number of times
print(str*5)

#slicing
print(str[-1:-4])
print(str[-1:0])
print(str[1:3])
print(str[:4])
print(str[1:])

#ord(): returns the ASCII code of the character
print(ord('A'))
print(chr(65))

print(ord('a'))
print(chr(97))

#len():
print(len("welcome"))
a=[1,2,3,4,5,5,6]
print(len(a))


#not in operator
print("come"not in a)

#string comparison character to character
print("tin"=="toe")
print("tin"!="toe")
print("tin">="toe")
print("tin"<="toe")
print("tic">"temp")
