N, M, K = map(int, input().split())
note = [[0]*M for _ in range(N)]

def isFitted(r, c, x, y, sticker):
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and note[x+i][y+j] == 1:
                return False
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and note[x+i][y+j] == 0:
                note[x+i][y+j] = 1
    return True


def rotate(r, c, sticker):
    transform = [[0]*r for _ in range(c)]
    p = r
    for i in range(r):
        p -= 1
        for j in range(c):
            transform[j][p] = sticker[i][j]
    return transform, c, r


for s in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    isfit = False
    for r in range(4):
        for i in range(N):
            if N - i < R:
                continue
            for j in range(M):
                if M - j < C:
                    break
                if isFitted(R, C, i, j, sticker):
                    isfit = True
                    break
            if isfit == True:
                break
        if isfit == True:
            break
        sticker, R, C = rotate(R, C, sticker)



result = 0
for i in range(N):
    for j in range(M):
        if note[i][j] == 1:
            result += 1
print(result)