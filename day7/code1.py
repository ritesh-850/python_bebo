#testing strings
# s = 'welcome to python'
# print(len(s))
# print(s.isalnum()) #isnum() contains number
#
# #isalpha() check the string contains only and only alphabet
# print(s.isalpha())
#
# #isdigit()
# print('2012'.isdigit())
#
# #isidentifier()
# print(s.isidentifier())
#
# #islower()
# print(s.islower())
# print('WELCOME'.isupper())
#
# #isspace()
# print(" ".isspace())

#log: 10 Searching in string
#startswith()
#endswith()
# s = "welcome to python"
# print(s.endswith("n"))
# print(s.startswith("w"))
#
# #.find()   index
# print(s.find("come"))
# print('hcome'.find("hello"))
#
# #.count() it will give no of occurence
# print(s.count('e'))


#log: 11 converting the strings
# s = "strings in python"
# print(s.capitalize())
#
# #title()
# print(s.title())
# #.lower()
# print(s.lower())
# #.upper()
# print(s.isupper())
# #.swapcase()
# print(s.swapcase())
# #.replace()
# print(s.replace("in","on"))

#log: 12 reverse the strings
#rev_str
#method 1
# s = "welcome"
# rev_str = ""
# for i in s:
#     rev_str = i + rev_str
#     print("the reverse of the string is:", rev_str)

#method2
# s = input()
# rev=s[::-1]
# if(s==rev):
#     print("palindrome")
# else:
#     print("not palindrome")
# #print(rev_str)
#
# s = input()
# rev=""
# for i in s:
#     rev = i+rev
# if s==rev:
#         print("palindrome")
# else:
#         print("not palindrome")

