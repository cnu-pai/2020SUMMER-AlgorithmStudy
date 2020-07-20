n, s = map(int, input().split())
arr = list(map(int, input().split()))
isused = [0 for _ in range(n)]
count = 0
def solution(i, total):
    global count
    if i == n:
        if s == total:
            count+= 1
        return
    solution(i+1, total)
    solution(i+1, total+arr[i])


solution(0, 0)
#s = 0 인경우, 공집합 제외
if s == 0:
    count -= 1
print(count)
