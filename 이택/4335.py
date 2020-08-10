# #글,숫자 입력받기
# #whlie(number!=0) : 리스트에 글하고 숫자 각각 추가
# #이중으로 whlie
# number=int(input(""))
# String=input("")
# while number!=0:
#     numberList=[]
#     StringList=[]
#     answerList=[]
#     while String != "right on":
#         numberList.append(number)
#         StringList.append(String)
#         number=int(input(""))
#         String=input("")
#         correct=number
#     for i in range(len(numberList)):
#         if numberList[i]>correct and StringList[i]=="too low":
#             answerList.append("Stan is dishonest")
#         elif numberList[i]<correct and StringList[i]=="too high":
#             answerList.append("Stan is dishonest")
#     if "Stan is dishonest" not in answerList:
#         print("Stan may be honest")
#     else:
#         print("Stan is dishonest")
#     number=int(input(""))
#     if number != 0 :
#         String=input("")

def _4335():
    Check = [True] * 11
    # print(Check[1])
    while 1:
        T = int(input())
        if T == 0:
            return
        S = str(input())
        if S == 'too high':
            for i in range(T, 11):
                Check[i] = False
        elif S == 'too low':
            for i in range(0, T+1):
                Check[i] = False
        else:
            if Check[T]:
                print('Stan may be honest')
            else:
                print('Stan is dishonest')
            Check = [True] * 11

_4335()