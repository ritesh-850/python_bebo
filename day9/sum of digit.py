n = int(input("Enter the number: "))
sum = 0
for i in range(1,n+1):
    rem = n%10
    sum+=rem
    n//=10
print(sum)