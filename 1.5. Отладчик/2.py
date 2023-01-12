"""
Псевдоним-пасьянс
"""

a = int(input())
b = 0
while a != 0:
    b = int(input())
    if b <= 3 and b <= a:
        a -= b
        print(a)
    else:
        print(a)
