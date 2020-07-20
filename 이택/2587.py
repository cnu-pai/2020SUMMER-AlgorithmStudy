NumberList = [int(input("")) for _ in range(5)]
average = (sum(NumberList)/len(NumberList))
print(int(average))
NumberList.sort()
mid = (len(NumberList)//2)
print(NumberList[mid])