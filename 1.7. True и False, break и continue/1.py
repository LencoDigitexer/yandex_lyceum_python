"""
Караул
"""

n = int(input())


while n != 0:
    if n == 0:
        break
    if n % 3 != 0 and n % 7 != 0:
        print(n)
    if n % 3 == 0 and n % 7 == 0:
        print('Караул!')
        break
    elif n % 3 == 0:
        print('несчастливое')
    elif n % 7 == 0:
        print('опасное')
    n = int(input())
