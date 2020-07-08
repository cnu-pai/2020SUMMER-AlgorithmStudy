from sys import stdin
a,b=map(int,stdin.readline().split())
list=[]
n=1
for i in range (1,50):
    for j in range(1,i+1):
        list.append(i)
sum=0;
for i in range(a-1,b):
    sum+=list[i]
print(sum)
