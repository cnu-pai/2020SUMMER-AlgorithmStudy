test = int(input())
for i in range(test):
    volunteer = int(input())
    score = [[0]*2 for _ in range(volunteer)]
    for j in range(volunteer):
        a, b = map(int, input().split())
        score[j][0] = a
        score[j][1] = b
    score = sorted(score, key=lambda x:x[0])
    cnt = 1
    min = score[0][1]
    for j in range(1, volunteer):
        if score[j][1] < min:
            min = score[j][1]
            cnt += 1
    print(cnt)
