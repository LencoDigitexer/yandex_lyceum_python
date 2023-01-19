"""
Подарок лепрекона
"""

last = ''
evil = good = 0

while (letter := input()) != '':
    if letter == 'Какой подарок?':
        if good > evil and last == 'добрый':
            print('серебряный шиллинг')
        elif good < evil and last == 'злой':
            print('золотой')
        else:
            print('Ах, не знаю!')
            break
        evil = good = 0
    elif letter == 'добрый':
        last = 'добрый'
        good += 1
    elif letter == 'злой':
        last = 'злой'
        evil += 1
    else:
        print('Неверный ввод')
