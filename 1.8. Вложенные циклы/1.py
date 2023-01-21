"""
Квадрат
"""

n = int(input())
i = 0

while (i < n * n):
    if i % n == 0 and i != 0:
        print()
    print(i + 1, end="\t")
    i = i + 1
