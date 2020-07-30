import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    PS = list(input())
    stack = []
    check = 0
    for parenthesis in PS:
        if parenthesis == '(':
            stack.append('(')
        elif parenthesis == ')':
            if len(stack) == 0:
                print('NO')
                check = 1
                break
            del stack[0]
    if check != 1:
        if len(stack) != 0:
            print('NO')
        else:
            print('YES')
