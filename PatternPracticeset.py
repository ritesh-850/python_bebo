# n = int(input("Enter the number:"))
# for i in range(n):
#     for j in range(i-1):
#         print("*",end=" ")
#     print()
#
#
# #
# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

#
n = int(input("Enter the number: "))
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    print()

#
# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print(k-1,end=" ")
#     print()
#
# #
n = int(input("Enter the number:"))
count = 1
for i in range(n):
    for j in range(n-i):
        print("",end="")
    for j in range(i+1):
        print(count,"",end="")
        count += 1
    print()