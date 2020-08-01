a=int(input(""))
total=0
decision=0
test5=a//5
test3=a//3
b=[]
c=[]
for i in range(test5+1):
    for j in range(test3+1):
        if a == 5*i + j*3:
            decision = 1 #decision이 1이 되면 설탕봉지를 맞출 수 있다는 뜻
            b.append(i)
            b.append(j)
if decision != 1:
    print(-1)
else:
    k=len(b)//2
    # print(f"len(b) : {len(b)}, k : {k}")
    if k == 0 : #b리스트에 2개밖에 없다면 그 두개를 합친 값이 정답
        print(sum(b))
    else:
        for i in range(len(b)):
            # print(i)
            if i%2 != 0:  #i가 홀수 일때는 넘어가고 짝수 일때 2개씩 덧셈을 하여 리스트에 추가
                pass
            else:
                value = b[i]+b[i+1]
                # print(c)
                c.append(value)
    print(min(c)) #c리스트에서 가장 작은 값이 답
# print(f"c : {c}")