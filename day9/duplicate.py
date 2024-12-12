list=[1,2,2,3,4]
for i in range(1,len(list)-1):
    if list[i]==list[i-1]:
        list.pop(i)
print(list)