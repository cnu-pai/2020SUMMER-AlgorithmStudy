# https://www.acmicpc.net/problem/1541
# User ID : thornsal
# Greedy

expression = input().split('-')
splitted_expression = list(map(lambda element: element.split('+'), expression))

result = sum(map(int, splitted_expression[0]))

for se in splitted_expression[1:]:
    result -= sum(map(int, se))

print(result)
