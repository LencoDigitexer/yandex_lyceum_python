"""
Слон или не слон?
"""

from math import inf

elephant = {'хобот': 1, 'хвост': 1, 'нога': 4, 'ухо': 2, 'глаз': 2, 'рот': 1}
*a, = iter(input, 'ОБЕД')
d = {}
for k, v in zip(a[1::2], map(int, a[::2])):
    d[k] = d.get(k, 0) + v
    if all(k in d for k in elephant) and \
       all(d[k] >= v for k, v in elephant.items()):
        break

count = inf
for k, v in elephant.items():
    if k in d:
        count = min(count, d[k] // v)
    else:
        print('Какие-то слоны нецелые. Пошли обедать.')
        break
else:
    if count == 0:
        print('Какие-то слоны нецелые. Пошли обедать.')
        exit()
    print('Есть слон!')
    print(count)
