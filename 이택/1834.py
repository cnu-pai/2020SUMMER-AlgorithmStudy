a = int(input(""))
namuzi = a-1 #나머지
Success=[]

for i in range(namuzi+1):
    if i==0:
        pass
    else:
        k = a*i+i
        Success.append(k)
        #print(Success)
print(sum(Success))
    # Meok = i // a
    # RealNamuzi = i % a
    # #print(f"몫 : {Meok}, 나머지 : {namuzi}")
    # if Meok == RealNamuzi:
    #     Success.append(i)
    #     #print(f"몫과 나머지가 같은 리스트 : {Success}")
# total = sum(Success)
# print(total)