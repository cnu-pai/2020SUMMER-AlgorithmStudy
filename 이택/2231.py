a=input("")
b=int(a)
#(1) 입력된것보다 작은수까지 range로 돌려서 생성자가 되는 것은 변수에 따로 추가하고
# 그 변수에서 가장 작은 수를 찾아 출력 --> 시간초과 걱정

store = []
for i in range(b):
    arbitrary = i
    k = str(i)
    for j in k:
        arbitrary += int(j)
    if arbitrary == b:
        store.append(i)
            #print(store)
print(f" 총 store : {store}")
if len(store)>=1:
    mini = min(store)
else :
    mini = 0
#print(f"store 작은 것 : {mini}")
print(mini)
#(2)생성자에서 분해합으로 가는 즉 거꾸로 가는 경우의 알고리즘 생각하여 만들기