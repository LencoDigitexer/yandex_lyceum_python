"""
Звездопад
"""

n = input()
a = []
while n != "ВСЁ":

    a.append(n)
    n = input()
word = 'звезд'
flag = False
for i, line in enumerate(a):
    if word in line.lower():
        print(i + 1)
        flag = True
        break

if not flag:
    print("НЕТ")
