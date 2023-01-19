"""
Мышиный хвост
"""

a = int(input())
b = int(input())
count = 0
countback = 0
flag = True
for i in range(b):
    x = input()
    if flag:
        if count + len(x) <= a:
            print(" " * count + x)
            count += 1
        else:
            print(" " * (a - len(x)) + x)
        if count + len(x) - a >= 1:
            countback += 1
            flag = False
    else:
        print(" " * (a - countback - len(x)) + x)
        if a - countback - len(x) <= 0:
            flag = True
            count = 1
            countback = 0
        else:
            countback += 1
