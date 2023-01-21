"""
Площадь
"""


def all_rec(n):
    i = 1
    while (i * i <= n):
        if n % i == 0:
            print(i, n // i)
        i += 1


n = int(input())
all_rec(n)
