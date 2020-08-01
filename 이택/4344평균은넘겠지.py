#1.케이스가 총 몇개인지 입력받는다
#2.각각 케이스마다 리스트로 입력받는다.
#3.(1)각 리스트의 첫번째 인덱스 빼고 모두 더한 뒤 첫번째 인덱스로 나눠 평균을 구한다
#4.(1)평균을 통해 평균이상 학생들 수를 구하고 그 비율을 구한다
#5.(1)반올림한다

def Ratio(caseList):
    total = sum(caseList)-caseList[0]
    average = total / caseList[0]
    count=0
    for i in range(len(caseList)):
        if i == 0:
            pass
        elif float(caseList[i])>average:
            count+=1
    ratio = (count / caseList[0] ) * 100
    rounding = round(ratio, 3)
    return rounding

caseNumber = int(input(""))
result=[]
for i in range(caseNumber):
    a=list(map(int,input("").split()))
    result.append(Ratio(a))
for i in result:
    print("%.3f"%i,end='')
    print("%")