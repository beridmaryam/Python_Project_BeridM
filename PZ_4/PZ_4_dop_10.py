# Вывести первые N (N >= 3) чисел Фибоначчи и посчитать количество четных чисел.

N = int(input('Введите количество чисел Фибоначчи (N >= 3): '))

f1 = 1
f2 = 1

print(f1)
print(f2)

kol_chet = 0

for i in range(N - 2):
    f_next = f1 + f2  
    print(f_next)
    
    if f_next % 2 == 0:
        kol_chet += 1
        
    f1 = f2
    f2 = f_next

print(f'Количество чётных чисел Фибоначчи: {kol_chet}')