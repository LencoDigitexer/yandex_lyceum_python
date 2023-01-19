"""
Yesterday
"""

a, count, max_count = input(), 0, 0
for _ in range(int(input())):
    if input() == a:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
else:
    if count > max_count:
        max_count = count

print(max_count)
