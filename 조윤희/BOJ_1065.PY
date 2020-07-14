import sys
input=sys.stdin.readline
def Han(n):
    cnt = 0
    if (n < 100):
        return n
    else:
        for i in range(100,(n+1)):
            hund = (i//100)
            ten = ((i%100)//10)
            one = ((i%100)%10)
 
            if ((hund - ten) == (ten - one)):
        cnt += 1
        return (99+cnt)
 
inp = int(input())
print(Han(inp)) 
