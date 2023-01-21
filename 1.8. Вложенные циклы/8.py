"""
Сомножители
"""

n = int(input())
res = [str(n)]
d = 2
while d <= n:
    if n % d == 0:
        res.append(str(d))
        n //= d
    else:
        d += 1
print(' * '.join(res).replace('*', '=', 1))
