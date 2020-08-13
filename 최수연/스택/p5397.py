import sys
input = sys.stdin.readline
test = int(input())

for i in range(test):
    L = list(input())[:-1]
    leftStack = []
    rightStack = []
    for j in range(len(L)):
        if L[j] == '<':
            if leftStack:
                rightStack.append(leftStack.pop())
        elif L[j] == '>':
            if rightStack:
                leftStack.append(rightStack.pop())
        elif L[j] == '-':
            if leftStack:
                leftStack.pop()
        else:
            leftStack.append(L[j])
    print(''.join(leftStack+list(reversed(rightStack))))
