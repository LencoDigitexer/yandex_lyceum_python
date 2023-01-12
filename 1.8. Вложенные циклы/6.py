"""
Последовательность Хэмминга
"""

n = int(input())
s = list(range(2, 6))
N1 = 0
while N1 < n:
    n2 = min(s)
    s.remove(n2)
    N1 += 1
    for i in range(2, 6):
        if n2 * i not in s:
            s.append(n2 * i)
print(n2)
