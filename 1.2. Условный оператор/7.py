"""
Который час?
"""

hour = input()

a = ["5", "6", "7", "8", "9", "10"]
b = ["11", "12", "13", "14", "15", "16", "17"]
c = ["18", "19", "20", "21", "22"]
d = ["23", "0", "1", "2", "3", "4"]

if hour in a:
    print("Утро")
elif hour in b:
    print("День")
elif hour in c:
    print("Вечер")
elif hour in d:
    print("Ночь")
else:
    print("Ошибка")
