a=list(map(int,input("").split()))
matrix1N=a[0]
matrix2N=a[1]
matrix1=[]
matrix2=[]
for i in range(matrix1N):
    matrix1.append(list(map(int,input("").split())))
for i in range(matrix1N):
    matrix2.append(list(map(int,input("").split())))
# print(matrix1)
# print(matrix2)
totalMarix=[]
for i in range(matrix1N):
    totalMarix.append([])
    for j in range(matrix2N):
        # print(matrix1[i][j],matrix2[i][j])
        totalMarix[i].append(matrix1[i][j]+matrix2[i][j])
for i in range(matrix1N):
    for j in range(matrix2N):
        print(totalMarix[i][j],end=' ')
    print()
# print(totalMarix)