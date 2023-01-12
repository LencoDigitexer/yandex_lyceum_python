"""
Вторые
"""

max, max2 = int(input()), int(input())
if max2 > max:
    max, max2 = max2, max
while True:
    t = int(input())
    if abs(t) >= 1000:
        break
    if t > max:
        max, max2 = t, max
    elif t > max2:
        max2 = t
print(max2)
