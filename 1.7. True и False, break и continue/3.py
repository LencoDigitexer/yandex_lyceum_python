"""
Звездопад
"""

n = input()
a = ""
while n != "ВСЁ":

    a = a + n
    n = input()

if "звезд" in a:
    print("Загадывай!")
else:
    print("НЕТ")
