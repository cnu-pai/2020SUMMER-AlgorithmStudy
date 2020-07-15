# https://www.acmicpc.net/problem/2200
# User ID : thornsal
# Greedy

n = int(input())
coefficients = list(reversed(list(map(int, (input().split()))))) # len = n +1

equal = 1
plus = n - coefficients.count(0)

count = plus + equal
acc_sum = 0

for i in range(n+1): # 0,1,2,3,....n
    if coefficients[i] != 0:
        if i == 0:
            count += len(str(coefficients[i]))
        else:
            if coefficients[i] != 1:
                count += 2*(i-acc_sum) + len(str(coefficients[i]))
                acc_sum += (i-acc_sum)
            else:
                count += 2 * (i - acc_sum - 1) + 1
                acc_sum += (i - acc_sum - 1)

print(count)













