a=input("").split()
b1=''
b2=''
k1=a[0]
k2=a[1]
for i in range(len(k1)-1,-1,-1):
    b1+=k1[i]
for i in range(len(k2)-1,-1,-1):
    b2+=k2[i]

if int(b1)>int(b2):
    print(b1)
else:
    print(b2)