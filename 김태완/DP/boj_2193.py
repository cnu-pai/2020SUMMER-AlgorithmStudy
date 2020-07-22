import sys

N = int(sys.stdin.readline())

my_list = [0 for _ in range(91)]  # use index 1~90

my_list[1] = 1
my_list[2] = 1

for i in range(3, N+1):
    my_list[i] = my_list[i-2] + my_list[i-1]

print(my_list[N])
