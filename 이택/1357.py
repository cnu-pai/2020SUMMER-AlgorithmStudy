number = input("").split()
V1=[]
V2=[]
for i in number[0]:
    V1.append(int(i))
for j in number[1]:
    V2.append(int(j))

def RV(VList):
    multiple = 1
    answer = 0
    for i in VList:
        answer += i*multiple
        multiple *= 10
    return answer

OneRV = str(RV(V1) + RV(V2))
OneRVList =[]
for k in OneRV:
    OneRVList.append(int(k))
TwoRV = RV(OneRVList)
print(TwoRV)