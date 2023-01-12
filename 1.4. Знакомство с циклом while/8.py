"""
Сократить дробь
"""

x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())
x_3 = x_1 * y_2 - x_2 * y_1
y_3 = y_1 * y_2
delitel = y_3
while delitel >= 1:
    a = y_3
    b = x_3
    while a % b != 0:
        c = a % b
        a, b = b, c
    delitel = b
    if x_3 % delitel == 0 and y_3 % delitel == 0:
        x_3 = x_3 // delitel
        y_3 = y_3 // delitel
    break
print(str(x_3) + "/" + str(y_3))
