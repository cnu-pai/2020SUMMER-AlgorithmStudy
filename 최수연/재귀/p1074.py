N, r, c = map(int, input().split())

def solution(n, r, c):
    if n == 0:
        return 0;
    half = pow(2, n-1)
    #1사분면
    if r < half and c < half:
        return solution(n-1, r, c)
    #2사분면
    elif r < half and c >= half:
        return solution(n-1, r, c - half) + half * half
    #3사분면
    elif r >= half and c < half:
        return solution(n-1, r - half, c) + 2 * half * half
    #4사분면
    return solution(n-1, r-half, c-half) + 3 * half * half

print(solution(N, r, c))