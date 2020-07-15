arr =[]
val = []
for i in range(int(input())):
    title = input()
    try: #제목 있을때
        val[arr.index(title)] += 1
    except: #제목이 없을때
        arr.append(title)
        val.append(1)

max_val = max(val)
max_arr = arr[val.index(max_val)]

for i in range(len(arr)): #팔린 권수 비교
    try: #최대 팔린 권수와 동일한 경우 있을때
        val[val.index(max_val)] = 0
        if max_arr>arr[val.index(max_val)]:
            max_arr = arr[val.index(max_val)]
    except Exception as e: #없으면 종료
        break
print(max_arr)
