T = int(input())
my_list = [0 for i in range(5)] # 0 1 2 3 4
my_list[1] = 1
my_list[2] = 2
my_list[3] = 4
my_list[4] = 7

for i in range(5, 11):
    my_list.append(sum(my_list[i-3:i]))

# n 은 1 부터 10 # 까지임..
for _ in range(T):
    print(my_list[int(input())])



