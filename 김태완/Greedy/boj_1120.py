# https://www.acmicpc.net/problem/1120
# User ID : thornsal
# Greedy


def compare(a, b):
    string_difference = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            string_difference += 1
    return string_difference


a, b = input().split(' ')
length_difference = len(b) - len(a)
minimum_string_difference = 50

for i in range(length_difference+1):
    minimum_string_difference = compare(a, b[i:]) if minimum_string_difference > compare(a, b[i:]) \
        else minimum_string_difference

print(minimum_string_difference)



