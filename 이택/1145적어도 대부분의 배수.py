number=list(map(int,input("").split()))
count=[0 for _ in range(5)]
total=1
answer=[]
for i in number:
    total*=i
for i in range(1,total+1):
    count = [0 for _ in range(5)]
    decision=0
    for j in range(len(number)):
        if i%number[j]==0:
            count[j]=1
    for j in range(len(number)):
        if count[j]==1:
            decision+=1
    if decision>=3:
        answer.append(i)
    if len(answer)==1:
        break

print(answer[0])