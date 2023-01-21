"""
Сдвиг
"""

string_1 = input()
string_2 = input()
is_possible = False
for i in range(len(string_1)):
    if string_1 == string_2:
        is_possible = True
        print(i)
    string_2 = string_2[1:] + string_2[0]
if not is_possible:
    print('NO')
