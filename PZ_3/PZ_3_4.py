#Ввести число. Если оно четное, разделить его на 4
# если нечетное - умножить на 5
a = input('Ведите число: ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input('Введите число: ')
 
if a % 2 == 0:
    d = a / 4
else:
    d = a * 5 

print(d)
