"""
Заводные жуки в квадрате
"""

a = float(input())
b = float(input())
n = 0
if a < b:
    print(n)
    exit()
while not abs(a - b) <= 0.01:
    a = (b**2 + (a - b)**2)**0.5
    n += 1
print(n)
