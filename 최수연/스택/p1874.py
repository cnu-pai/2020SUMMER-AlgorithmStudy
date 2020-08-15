n = int(input())

incre = 1
stack = []
cnt = 0
result = []
for i in range(n):
    num = int(input())
    if stack and stack[-1] == num:
        stack.pop()
        result.append("-")
        cnt += 1
        continue
    else:
        for j in range(incre, num+1):
            stack.append(incre)
            incre += 1
            result.append("+")
    if stack[-1] == num:
        stack.pop()
        result.append("-")
        cnt += 1

if cnt == n:
    for i in result:
        print(i)
else:
    print("NO")