# Дано вещественно число - цена 1 кг конфет.
# Вывести стоимость 1, 2, ..., 10 кг.

cena_konfet = input('Введите цену за 1 кг конфет: ')

while type(cena_konfet) != float:
    try:
        cena_konfet = float(cena_konfet)
    except ValueError:
        print('Неправильно ввели!')
        cena_konfet = input('Введите цену за 1 кг конфет: ')

kg = 1

while kg <= 10:
    stoimost = cena_konfet * kg
    print(f"Стоимость {kg} кг конфет: {stoimost:.2f} руб.")
    kg += 1


