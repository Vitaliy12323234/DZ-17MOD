per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
stavka = per_cent.values()
stav = list(stavka)
summa = float(input('Введите сумму:'))
print('Вы можете заработать:', stav[0] * summa / 100, stav[1] * summa /100, stav[2] * summa / 100, stav[3] * summa/ 100)
max_stavka = max(stav)
print('Максимум можно заработать:', max_stavka * summa / 100)