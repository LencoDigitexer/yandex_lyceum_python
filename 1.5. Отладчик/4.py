"""
Кролики
"""

f1 = 1
f2 = 1
i = 0
n = int(input())
while f2 < n:
    f1, f2 = f2, f1 + f2
    i = i + 1
if f2 != n:
    print("НЕТ")
else:
    print(i + 2)
