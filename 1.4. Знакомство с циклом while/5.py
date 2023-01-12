"""
Богатенький Буратино
"""

price, s, i = int(input()), 1, 0
while s <= price:
    if price == 1:
        break
    s *= 10
    i += 1

print(i)
