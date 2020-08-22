number=int(input(""))
count=0
for i in range(number):
    de=0
    st=list(map(str,input("")))
    Sst = set(st)
    q={}
    w=[]
    for j in Sst:
        q[j]=0
    for j in range(len(st)):
        name=st[j]
        if j==len(st)-1 :
            break
        q[name]+=1
        if q[name] != 1: #띄어져서 또 같은 글자가 나오는지 확인하는 역할
            q[name]=-13
        elif st[j+1]==st[j]: #다음문자가 현재 글자와 같다면 딕셔너리에서 그 글자의 값을 0으로 만들어 최종적으로는 그 글자의 값이 1이 되게함
            #만약 연속되지않고 그다음에 같은 문자가 나온다면 1이 아닌 다른 값이 나오게 됨.
            q[name]=0
    imit =st[len(st)-1]
    q[imit]+=1
    if q[imit] != 1:
        q[imit]=-13
    for j in q:
        if q[j]!=1:
            de=-1
    if de==-1:
        pass
    else:
        count+=1
print(count)