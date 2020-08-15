import copy

number=int(input(""))
all = [input("") for _ in range(number)]
Printing=[]
def short(all):
    mini = 51
    for i in all:
        if len(i)<mini:
            mini=len(i)
    imit=copy.deepcopy(all)
    add=[]
    for n,v in enumerate(all):
        if len(v)==mini:
            add.append(v)
            imit.remove(v)
    return add,imit

def printing(add,Printing):
    add.sort()
    In=Printing
    for i in add:
        if i in In:
            pass
        else:
            print(i)
            In.append(i)
    return In
while all:
    add,all=short(all)
    Printing=printing(add,Printing)