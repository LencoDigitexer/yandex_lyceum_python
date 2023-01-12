"""
Каникулы капризного ребёнка
"""

town1 = input()
town2 = input()

tula = 'Тула'
penz = 'Пенза'

if town1 != town2 and (town1 == tula and town2 != penz
                       or town2 == penz and town1 != tula):
    print('ДА')
else:
    print('НЕТ')
