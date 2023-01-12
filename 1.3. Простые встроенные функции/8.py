"""
Небоскрёбы
"""

out = ''
tmp = 0
for i in range(1, 6):
    k = int(input())
    if k > tmp:
        out += str(i) + ' '
        tmp = k
print(out)
