StrNumber=(input(""))
long = len(StrNumber)
Number=int(StrNumber)
name=""
DN=0
for i in range(1,Number+1):
    name+=str(i)
print(name)
NameLong = len(name)
for n,v in enumerate(name):
    decision = ""
    if n == (NameLong-long):
        decision += name[n:n + long]
        if decision == StrNumber:
            DN = n + 1
        break
    else:
        decision+=name[n:n+long]
    print(f"결정하는 값: {decision}")
    if decision == StrNumber:
        DN=n+1
        break
print(DN)
