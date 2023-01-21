"""
Многоножки
"""

more_than_40 = set()
even = set()
multiple_of_3 = set()
for i in range(int(input())):
    num = int(input())
    if num > 40:
        more_than_40.add(num)
    if num % 2 == 0:
        even.add(num)
    if num % 3 == 0:
        multiple_of_3.add(num)
print(*((more_than_40 & even | even & multiple_of_3
         | multiple_of_3 & more_than_40) -
        (more_than_40 & even & multiple_of_3)))
