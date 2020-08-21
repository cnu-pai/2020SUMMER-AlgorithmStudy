def checkSentence(sentence, stack):
    for w in sentence:
        if w == '[':
            stack.append('[')
        elif w == '(':
            stack.append('(')
        elif w == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return 1
        elif w == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 1
    if stack:
        return 1
    return 0


while True:
    sentence = input()
    if sentence == '.':
        break
    stack = []
    balance = checkSentence(sentence, stack)
    if balance:
        print('no')
    else:
        print('yes')
