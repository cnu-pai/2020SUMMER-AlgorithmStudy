import sys

T = int(input())

for _ in range(T):
    count = 1
    applicant_number = int(input())
    d = sorted([tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(applicant_number)])

    m = d[0][1]

    # more pythonic

    for x in [d[i][1] for i in range(applicant_number)][1:]:
        if m > x:
            count += 1
            m = x
    print(count)

    # previous one : count = 0

    # for i in range(applicant_number):
    #     if i == 0:
    #         count += 1
    #     else:
    #         if m > d[i][1]:
    #             count += 1
    #             m = d[i][1]

