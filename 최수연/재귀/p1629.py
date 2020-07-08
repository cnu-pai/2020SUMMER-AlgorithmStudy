A, B, C = map(int, input().split())

def multiply(a, b, c):
    if b == 0:
        return 1 % c
    if b == 1:
        return a % c
    if b % 2 == 0:
        return pow(multiply(a, b//2, c), 2) % c
    else:
        return (multiply(a, b//2, c) * multiply(a, b//2 + 1, c)) % c

print(multiply(A, B, C))