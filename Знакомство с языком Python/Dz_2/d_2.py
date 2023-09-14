# x = abs(int(input('Введите первое натуральное число X ')))
# y = abs(int(input('Введите второе натуральное число Y ')))
# S = x + y
# P = x * y
# y1 = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
# x1 = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
# print(x1, y1)


x = abs(int(input('Введите первое натуральное число X от 1 до 1000 ')))
y = abs(int(input('Введите второе натуральное число Y от 1 до 1000 ')))
if x < 1 or x > 1000 or y < 1 or y > 1000:
    print('Вы ввели число не из заданного диапазона!')
else:
    S = x + y
    P = x * y
    stop = 0
    for i in range(1001):
        if stop != 1:
            for j in range(1001):
                if stop != 1:
                    if i * j == P and i + j == S:
                        print(i, j)
                        stop = 1
            else:
                j = 1001
        else:
            i = 1001