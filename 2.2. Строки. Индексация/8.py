"""
Резиновые слова
"""

a = input()
t = len(a) // 2
if (len(a) % 2):
    print(' ' * t + a[t])
for i in range(t - 1, -1, -1):
    print(' ' * i + a[i] + ' ' * (len(a) - 2 * i - 2) + a[-i - 1])
