"""
Ряд
"""

a = int(input())

i = a

for j in range(0, 4):
    i = i + 1
    a = a + i
    i = i + 1
    a = a * i

print(a)
