import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque()
for i in range(N):
    command = list(map(str, input().split()))
    if command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print('-1')
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue:
            print('0')
        else:
            print('1')
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print('-1')
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        queue.append(command[1])