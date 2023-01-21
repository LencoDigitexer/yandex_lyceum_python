"""
Примеры
"""

t = int(input())
k = int(input())
f = int(input())

for i in range(t, k + 1, f):
    for j in range(t, k + 1, f):
        print(f'{i} + {j} = {i + j}', end='\t')
    print()
