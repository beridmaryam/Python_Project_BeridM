# Ввести 4 числа.
# Найти и вывести на экран сумму и количество отрицательных чисел
sum = 0
kol = 0

for i in range(4):
    num = float(input('Введите число: '))
    if num < 0:
        kol = kol + 1
        sum = sum + num

print(f'Количество: {kol}')
print(f'Сумма: {sum}')