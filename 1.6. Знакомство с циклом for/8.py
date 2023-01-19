"""
Без ударения
"""

stroka = input()

vowel = 'аяоёэеуюыи'

flag = False

cnt = 0

for w in stroka:
    if w == ' ':
        flag = False
    elif w in vowel:
        if flag:
            cnt += 1
        else:
            flag = True

print(cnt)
