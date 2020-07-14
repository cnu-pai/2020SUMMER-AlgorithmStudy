import sys
sys.stdin=open('input.txt',"r")
input=sys.stdin.readline
arr =[]
val = []
for i in range(int(input())):
    title = input()
    try: #제목 있을 때
        val[arr.index(title)] += 1
    except: #제목 없을 때
        arr.append(title)
        val.append(1)

max_val = max(val)
max_arr = arr[val.index(max_val)]

for i in range(len(arr)): #팔린 책 수
    try: #중복이면
        val[val.index(max_val)] = 0
        if max_arr>arr[val.index(max_val)]:
            max_arr = arr[val.index(max_val)]
    except Exception as e: #없우면 종료
        break 
print(max_arr)
