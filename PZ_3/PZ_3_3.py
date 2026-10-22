# ввести два числа. Если их произведение отрицательно, умножить на 8
# в протвном случае увеличить его в 1.5 раз

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

c = a * b 
if c<0:
    d = c * 8
else:
    d = c * 1.5 

print(d)

