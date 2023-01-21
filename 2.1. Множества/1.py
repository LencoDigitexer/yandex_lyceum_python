"""
Каталог
"""

titles = set()
for i in range(int(input())):
    title = input()
    if title not in titles:
        print('НЕТ')
        titles.add(title)
    else:
        print('ДА')
