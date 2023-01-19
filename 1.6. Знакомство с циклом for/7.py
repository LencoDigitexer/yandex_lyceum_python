"""
Сантикилометр
"""
s = input()
p = 2
for w in s:
    if w == 'с':
        p -= 2
    elif w == 'к':
        p += 3
res = 10**abs(p)
if p < 0:
    print('1/', end='')
print(res)
