number = int(input(""))
FName = {chr(x) : 0 for x in range(97,123)}  #성 : 개수 딕셔너리로 만들기
SaveList = [input("") for _ in range(number)] #선수 성,이름 저장
Participate = []

#print(SaveList)
for i in SaveList:  #선수들 성 개수에 맞게 성딕셔너리에 있는 성에 +1해준다
    if i[0] in FName:
        FName[i[0]]+=1
#print(FName)

for i in FName: #같은 성이 5개 있다면 그 성을 출전리스트에 넣기
    if FName[i] >= 5 :
        Participate.append(i)
else:
    if len(Participate)>=1:
        for i in Participate:
            print(i,end="")
    else:
        print("PREDAJA")