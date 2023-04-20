import math

def simple_num(num) -> bool:
    if num == 2:
        return 1
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return 0
    return 1


num = int(input("Введите число: "))
if num == 1 or num == 0:
    print("Не является ни простым, ни составным")
else:
    if simple_num(num):
        print("Простое")
    else:
        print("Составное")