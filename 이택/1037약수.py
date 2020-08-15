import math
count = int(input(""))
number = list(map(int,input("").split()))
number.sort()
answer = []
for i in range(count):
    oppsiteCount=count-i-1
    if count%2 == 0:
        if i == count//2:
            break
    else:
        if i == math.ceil(count/2):
            break
    answer.append(number[i]*number[oppsiteCount])
correct=answer[0]
decision = 0
for i in answer:
    if correct != i:
        decision = -1
if decision != -1:
    print(correct)