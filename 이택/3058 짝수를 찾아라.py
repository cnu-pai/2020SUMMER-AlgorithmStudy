a=int(input(""))
def NOdd(a):
    b=[]
    for i in a:
        if i%2==0:
            b.append(i)
    return b
answer=[]
total=[]
for i in range(a):
    l = []
    k=list(map(int,input("").split()))
    l=NOdd(k)
    answer.append(min(l))
    total.append(sum(l))
for i in range(len(total)):
    print(total[i],answer[i])