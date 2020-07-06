# https://www.acmicpc.net/problem/2217
# User ID : thornsal
# Greedy

rope_number = int(input())
rope_capability = []
weight = 0

for _ in range(rope_number):
    rope_capability.append(int(input()))

rope_capability.sort(reverse = True)

# upgraded : more pythonic
print(max(rope_capability[i]*(i+1) for i in range(rope_number)))

# previous one

# for i in range(rope_number):
#     new_weight = rope_capability[i] * (i+1)
#     if new_weight > weight:
#         weight = new_weight
#
# print(weight)



