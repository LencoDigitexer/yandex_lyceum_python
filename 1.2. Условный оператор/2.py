"""
Да или нет?!
"""

x = input()
y = input()

data = ['да', 'нет']
if x.lower() in data and y.lower() in data:
    print("ВЕРНО")
else:
    print('НЕВЕРНО')
