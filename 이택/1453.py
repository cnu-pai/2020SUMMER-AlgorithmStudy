number = int(input(""))
charge = list(map(int,input("").split()))
seat = []
count = 0
for i in charge:
    if i in seat:
        count += 1
    else:
        seat.append(i)
print(count)