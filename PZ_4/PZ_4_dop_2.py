# Ввести 4 числа. Найти и вывести на экран количество четных чисел.

kol = 0

for i in range(4):
    num = float(input('Введите число: '))
    if num > 0:
        kol = kol + 1

print(f'Количество: {kol}')