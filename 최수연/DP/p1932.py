n = int(input())
route = [[0] * 2 for _ in range(n)]
triangle = list()
for i in range(n):
    temp = list(map(int, input().split()))
    triangle.append(temp)
    if i == 0:
        triangle[0][0] = temp[0]
    else:
        for j in range(len(triangle)):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i-1][j - 1], triangle[i-1][j])

print(max(triangle[i]))