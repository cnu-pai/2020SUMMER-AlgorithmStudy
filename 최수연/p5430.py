from collections import deque
import re
T = int(input())
deque = deque()

for i in range(T):
    p = list(str(input()))
    n = int(input())
    numList = re.findall("\d+", str(input()))
    for j in range(len(numList)):
        deque.append(int(numList[j]))
    check = 0
    for j in range(len(p)):
        if p[j] == 'R':
            if check == 0:
                check = 1
            elif check == 1:
                check = 0
        else:
            if deque:
                if check == 0:
                    deque.popleft()
                elif check == 1:
                    deque.pop()
            else:
                check = 2
                print('error')
                break
    if check == 1:
        deque.reverse()
    if check != 2:
        print('[', end='')
        for j in range(len(deque)-1):
            print(deque[j], end=',')
        if deque:
            print(deque[-1], end='')
        print(']')
    deque.clear()

