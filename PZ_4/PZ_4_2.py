# Дано целое число N(>0)
# определить имеется ли в записи числа N цифра 2.
# Если имеется ввести TRUE, если нет - вывести FALSE.

n = input("Введите целое положительное число N: ")

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите целое положительное число N: ")

while n > 0 and n % 10 != 2:
    n = n // 10

if n > 0:
    print("TRUE")
else:
    print("FALSE")
