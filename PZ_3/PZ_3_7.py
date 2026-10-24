# Дано два числа. Если их сумма кратна 5, то прибавить 1
# иначе вычесть 2

a = input('Ведите первое число: ')
b = input('Ведите второе число: ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input('Введите первое число: ')

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Неправильно ввели!')
        b = input('Введите второе число: ') 

c = a + b 
if c % 5 == 0:
    d = c + 1
else:
    d = c - 2 

print(d)

