"""
Гуси, утки, куры
"""

n = int(input())
m = int(input())
nm = m - 7 * n
kx = nm // 18
for x in range(kx + 1):
    y = (nm - 18 * x) // 3
    if 18 * x + 3 * y == nm and y >= 0:
        z = n - x - y
        if z >= 0:
            print(x, y, z)
