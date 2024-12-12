#game that has a random value and we have to guess the number if num==guess print "guessed" in count and the real number is "R"
import random
r=random.randint(1,100)
# print(r)
count = 0

while True:
    n = int(input("Enter any number: "))
    count+=1
    if(n==r):
        print(f"congrats, you win the game in step {count}")
        break
    elif(n<r):
        print("Enter high number")
    else:
        print("Enter low number")