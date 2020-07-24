a=input("")
b=[]
change=[]
small=[chr(x) for x in range(97,123)]
big=[chr(x) for x in range(65,91)]
# print(small)
# print(big)
for i in a:
    b.append(i)
for i in b:
    if i in big:
        change.append(i.lower())
    elif i in small:
        change.append(i.upper())
    # print(change)
k=''
for i in change:
    k+=i
print(k)