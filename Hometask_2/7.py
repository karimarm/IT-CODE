def fibonachi(num) -> int:
    if num == 1:
        return 0
    a = 0
    b = 1
    for i in range(2, num):
        a, b = b, a
        b += a
    return b

num = int(input("Введите число: "))
if num > 0:
    print(fibonachi(num))