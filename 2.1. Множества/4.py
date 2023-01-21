"""
Оркестр
"""

goboe = set()
fleit = set()
sacksofon = set()
surname = input()
while surname:
    goboe.add(surname)
    surname = input()
surname = input()
while surname:
    fleit.add(surname)
    surname = input()
surname = input()
while surname:
    sacksofon.add(surname)
    surname = input()
for item in goboe.symmetric_difference(fleit).symmetric_difference(
        sacksofon) - (goboe & fleit & sacksofon):
    print(item)
