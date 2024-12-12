# Print factorial of numbers
def fact(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#fibonacci series
def fibonacci(n):
    a = 0
    b = 1
    c = 0
    print(a)
    print(b)
    for i in range(0,n-2):
        c=a+b
        a=b
        b=c
    return fibonacci (n)
print(fibonacci(4))