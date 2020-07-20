NumberList = [int(input("")) for _ in range(10)]
NSet = set(NumberList)
NDict = {}
deicision=[]

for i in NSet:#딕셔너리 key와 value설정
    NDict[i]=0

for j in NumberList:#개수에 맞게 value 설정
    NDict[j] += 1

average = int(sum(NumberList)/(len(NumberList)))

maxi =0
name =0

for n,v in enumerate(NDict): #빈도수 가장 많은 수의 이름을 name변수에 넣기
    if NDict[v] > maxi:
        maxi = NDict[v]
        name = v

print(average)
print(name)