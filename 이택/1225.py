a=input().split()
first = a[0]
second = a[1]
total = 0
f=[]
s=[]

for i in first:
    f.append(int(i))
for j in second:
    s.append(int(j))
total = (sum(f)*sum(s))
print(total)



# for i in first:
#     for j in second:
#         total += int(i)*int(j)
        # print(f"i : {i},  j : {j}")
        # print(total)
# print(int(total))
