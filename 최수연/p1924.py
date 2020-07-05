def getDay(x):
    return {0:'SUN', 1:'MON', 2:'TUE', 3:'WED', 4:'THU',5:'FRI', 6:'SAT'}.get(x)

month, date = map(int, input().split())
sum = date
if month == 1:
    day = date
else:
    for i in range(1, month):
        if i == 2:
            sum+= 28
        elif i == 4 or i == 6 or i == 9 or i == 11:
            sum += 30
        else:
            sum += 31



print(getDay(sum%7))
