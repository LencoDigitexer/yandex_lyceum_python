"""
Экономия
"""

digits = set()
for i in range(int(input())):
    n = int(input())
    while n > 0:
        digits.add(n % 10)
        n //= 10
print(len(digits))
