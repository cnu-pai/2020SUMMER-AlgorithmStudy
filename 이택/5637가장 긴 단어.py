exsistent=[]
for i in range(65,91):
    exsistent.append(chr(i))
for i in range(97,123):
    exsistent.append(chr(i))
exsistent.append("-")

max=0
answer=[]
while True:
    a=input("").split()
    answer+=a
    # print(answer)
    if "E-N-D" in answer:
        break
ranswer=[]
for n,i in enumerate(answer):
    k=i
    q=''
    for j in k:
        if j in exsistent:
            q+=j
    ranswer.append(q)
# print(ranswer)

correct=[]
for i in ranswer:
    if len(i)>max and i != "E-N-D":
        max=len(i)

for i in ranswer:
    if len(i)==max:
        correct.append(i);
print(correct[0].lower())