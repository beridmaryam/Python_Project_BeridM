# Ввести N чисел. Найти и вывести их среднее арифметическое.

N = int(input('Сколько чисел вы хотите ввести? '))
print(f'Пожалуйста, введите {N} чисел по очереди:')

sum = 0

for i in range(N):
    chislo = float(input(f'Введите {i + 1}-е число: '))
    sum = sum + chislo

srednee = sum / N

print(f'Среднее арифметическое равно: {srednee}')