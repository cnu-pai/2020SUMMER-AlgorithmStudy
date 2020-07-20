a=list(map(int, input("").split()))
NewBinary_a=0
ten_a1=0
ten_a2=0

def ten_binary(number):
    multiple = 1
    answer = 0
    while number>0:
        answer += (number%2)*multiple
        multiple *= 10
        number = number // 2
    return  answer

def binary_ten(number):
    answer = 0
    multiple = 1
    while number > 0:
        answer += (number%10)*multiple
        multiple *= 2
        number = number // 10
    return answer

ten_a1 = (binary_ten(a[0]))
ten_a2 = ((binary_ten(a[1])))

total = ten_a1 + ten_a2
NewBinary_a = ten_binary(total)
print(NewBinary_a)