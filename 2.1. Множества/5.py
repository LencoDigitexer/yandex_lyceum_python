"""
Все цифры
"""

n = set(input())
numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
for item in n:
    numbers.discard(item)
for item in numbers:
    print(item, end=' ')
