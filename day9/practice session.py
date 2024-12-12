#---------fizzbuzz------------
# for i in range(1,16):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 5 == 0:
#         print("buzz")
#     elif i % 3 == 0:
#         print("fizz")
#     else:
#         print(i)

#------------Sum of digit------------------
# n = int(input("Enter the number: "))
# sum = 0
# for i in range(1,n+1):
#     rem = n%10
#     sum+=rem
#     n//=10
# print(sum)

#--------------duplicate-------------------
# list=[1,2,2,3,4,4,5,5]
# for i in range(1,len(list)-1):
#     if list[i]==list[i-1]:
#         list.pop(i)
# print(list)

# list=[1,2,2,3,4,4]
# def remove_duplicate(lst):
#     result=[]
#     for i in lst:
#         if i not in result:
#             result.append(i)
#         return result
# print(remove_duplicate(list))

# list = list(map(int,input("enter list..").split(",")))
# i=0
# while(i<len(list)):
#     j=i+1
#     while(j<len(list)):
#         if list[i]==list[j]:
#             list.pop(j)
#         else:
#             j=j+1
#     i=i+1
# print(list)

#--------------max tuple------------
# mytuple=(4,1,8,3,9)
# def min_max_tuple(n):
#     min=n[0]
#     max=n[0]
#
#     for i in n:
#         if i<min:
#             min=i
#         elif i>max:
#             max=i
#     # else:
#     #     print("Error")
#     return(min,max)
# print(min_max_tuple(mytuple))
#
# tuple = (4,1,8,3,9)
# min = max = tuple[0]
# for i in tuple:
#     if i < min:
#         min = i
#     if i > max:
#         max = i
# res = (min,max)
# print(res)

#----------------------------prime numbers--------------------
# def prime_no():
#     start=int(input("enter the no: "))
#     end=int(input("enter the no: "))
#     prime=[]
#     for i in range(start,end+1):
#         if i>1:
#             is_prime=True
#             for num in range(2,int(i**0.5)+1):
#                 if i%num==0:
#                     is_prime=False
#                     break
#             if is_prime:
#                 prime.append(i)
#     return prime
# primes=prime_no()
# print(primes)
#

start = int(input("Enter the start of the range: "))

end = int(input("Enter the end of the range: "))
primes = []


for num in range(start, end+1):
    if num > 1:
        isPrime = True
        for i in range(2,num):
            if num % i == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(num)
print(f"Prime numbers between {start} and {end}: {primes}")


# #----------------first word capitalize-----------------
# s="hello everyone present here"
# word=s.split()
# title=' '.join(i.capitalize() for i in word)
# print(title)