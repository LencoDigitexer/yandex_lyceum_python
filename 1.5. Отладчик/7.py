"""
Сложные проценты
"""

n = int(input())
p = float(input())
t = float(input())
for i in range(int(t // 1)):
    n += (n / 100) * p
if t == t // 1:
    print(n)
    exit()
x = t - (t // 1)
n += n * x * 0.01
print(n)
