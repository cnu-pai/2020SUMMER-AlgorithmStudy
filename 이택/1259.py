a=[]
a.append(input(""))
while int(a[-1])!=0:
    a.append(input(""))
# print(a)
count=-1
while True:
    count+=1
    imit=a[count]
    k=''
    for i in range(len(imit)-1,-1,-1):
        k+=imit[i]
    # print(k)
    if int(k)==0:
        break
    if(k==imit):
        print("yes")
    else:
        print("no")