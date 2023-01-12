"""
Холмы
"""

p = int(input())
c = int(input())
r = 0
while True:
    n = int(input())
    if n == -1:
        print(r)
        break
    if c > p and c > n:
        r += 1
    p, c = c, n
