"""
По порядку рассчитайсь!
"""
n = input()
a = []
for i in range(0, int(n)):
    b = input()
    a.append(b)

for i in range(0, int(n)):
    print(str(i + 1), a[i])
