per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
stavka = per_cent.values()
summa = float(input('Введите сумму:'))
for procent in stavka:
    deposit = (round(procent / 100 * summa))
    print('Вы заработаете:', deposit)
stav = list(stavka)
max_stav = float(max(stav))
print('Вы заработаете максимум:', max_stav * summa / 100)

