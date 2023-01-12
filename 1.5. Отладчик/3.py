"""
Черная пятница
"""

a = int(input())


def sale(percent):
    res = 0
    if not percent:
        res = 50
    elif percent <= 30:
        res = percent + (percent // 2)
    elif 30 < percent <= 70:
        res = percent + (percent * .1)
    else:
        res = percent
    return int(res)


print(sale(a))
