"""
Выше и ниже
"""

k = int(input())
b = int(input())
ko, kl, ku = 0, 0, 0
x = input()
while x != 'END':
    x = int(x)
    y = int(input())
    d = y - b - k * x
    if d < 0:
        ku += 1
    elif d > 0:
        ko += 1
    else:
        kl += 1
    x = input()
if ko:
    print('Выше прямой:', ko)
if ku:
    print('Ниже прямой:', ku)
if kl:
    print('На прямой:', kl)
