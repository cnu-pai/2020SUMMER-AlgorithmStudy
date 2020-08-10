a=int(input(""))
def _1526(q):
    a=list()
    c=[1,2,3,5,6,8,9,0]
    for i in range(4,q+1):
        decision=0
        l=list(map(int,str(i)))
        for k in l:
            if k==4 or k==7:
                pass
            else:
                decision = 1
        if decision == 0 :
            a.append(i)
    return a
print(max(_1526(a)))