"""
Только минус
"""

count = 0
while (x := float(input())) <= 36.6:
    if x < 0:
        count += 1
print(count)
