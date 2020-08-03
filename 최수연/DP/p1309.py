size = int(input())
zoo = [[0]*2 for _ in range(size)]
zoo[0][0], zoo[0][1] = 1, 1
for i in range(1, size):
    zoo[i][0] = zoo[i-1][0] + zoo[i-1][1]*2 % 9901
    zoo[i][1] = zoo[i-1][0] + zoo[i-1][1] % 9901

print((zoo[size-1][0] + zoo[size-1][1]*2) % 9901)