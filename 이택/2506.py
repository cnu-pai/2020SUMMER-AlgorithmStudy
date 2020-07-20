a=int(input(""))
b=[int(x) for x in input("").split()]
k=0
sum=0
for i in b:
    if i == 1:
        k+=1
        sum+=k
    elif i == 0:
        k=0
print(sum)