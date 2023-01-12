"""
Ним2-пасьянс
"""

a = int(input())
b = int(input())

while a != 0 or b != 0:
    n = int(input()) - 1
    c = int(input())

    if n:
        b -= c
        print(a, b)
    else:
        a -= c
        print(a, b)
