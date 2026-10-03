# дано скорость лодки в стоячей воде, скорость течение реки и время движение реки по течению и против теченя.
# определить путь S, пройденый лодки. Учесть что против течении скорсть уменьшается на велечину скорости течения.
#U < V
while True:
    try:
        V = float(input("Введите скорость лодки (V, км/ч): "))
        break
    except ValueError:
        print('error')

while True:
    try:
        U = float(input("Введите скорость течения (U, км/ч): "))
        break
    except ValueError:
        print('error')

while True:
    try:
        T1 = float(input("Введите время на озере (T1, ч): "))
        break
    except ValueError:
        print('error')

while True:
    try:
        T2 = float(input("Введите время по реке (T2, ч): "))
        break
    except ValueError:
        print('error')

if U < V:
    S1 = V * T1
    V_prot_tech = V - U
    S2 = V_prot_tech * T2
    S = S1 + S2
    print("Общий путь лодки составляет:", S, "км")
else:
    print("Скорость течения реки должна быть меньше скорости лодки!")




