# # no is palindrome
# n = int(input("Enter the numbers : "))
# temp = n
# rev = 0
# while temp > 0:
#     rem = temp % 10
#     rev = (rev * 10)+ rem
#     temp = temp // 10
# if n == rev:
#     print("no is palindrome")
# else:
#     print("not palindrome")
#
# #sting name palindrome
# s = str(input("Enter the string : "))
# if (s==s[::-1]):
#     print("Is Palindrome")
# else:
#     print("not palindrome")
#
# #fibonacci series
# n = 5
# a , b = 0,1
# temp = 0
# for i in range(n+1):
#     print(a)
#     temp = a
#     a = b
#     b = temp + b
# print()


#Pattern --- up-stair
# n = int(input("Enter the number : "))
# for i in range(n+1):
#     for j in range(i):
#         #for j in range(n+i):
#             print("*",end=" ")
#     print()

#pattern -------up-stair-down
# n = int(input("Enter the number : "))
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

#pattern ------ down-stair-down
# n = int(input("enter the number : "))
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print("*",end=" ")
#     print()

#pattern
# n = int(input("Enter the number : "))
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n+i):
#         print("*",end=" ")
#     print()
#
#pattern ---- star
n = int(input("Enter the number : "))
for i in range(n-1):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        print("*",end=" ")
    for l in range(n-i-1):
        print("*",end=" ")
    print()