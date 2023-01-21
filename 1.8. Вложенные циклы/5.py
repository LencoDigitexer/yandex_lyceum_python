"""
Сумма степеней
"""

n = int(input())
s = 0
for i in range(1, n + 1):
    s += pow(i, sum(range(i % 2, i + 1, 2)))
print(s)
