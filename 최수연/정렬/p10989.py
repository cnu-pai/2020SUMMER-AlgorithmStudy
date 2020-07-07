import sys
input = sys.stdin.readline
N = int(input())
bucket = [0] * 10001
def CountingSort():
    for i in range(N):
        num = int(input())
        bucket[num] += 1

    for k in range(10001):
        if bucket[k] != 0:
            for l in range(bucket[k]):
                print(k)

CountingSort()
