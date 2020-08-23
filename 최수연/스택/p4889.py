idx = 1
while True:
    data = list(input())
    if data[0] == '-':
        break
    stack = []
    for c in data:
        if stack and stack[-1] == '{' and c == '}':
            stack.pop()
        else:
            stack.append(c)
    if stack:
        ans = 0
        while stack:
            x = stack.pop()
            y = stack.pop()
            if x == y:
                ans += 1
            else:
                ans += 2
        print(str(idx)+".", ans)
    else:
        print(str(idx)+".", 0)
    idx += 1