per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
stavka = per_cent.values()
summa = float(input('Введите сумму:'))
for procent in stavka:
    deposit = (round(procent / 100 * summa))
    print('Вы заработаете:', deposit)

