"""
Регистрация почты
"""

login = input()
email = input()
if "@" in email and "@" not in login:
    print('OK')
else:
    if "@" in login:
        print('Некорректный логин')
        exit()
    if "@" not in email:
        print('Некорректный адрес')
        exit()
