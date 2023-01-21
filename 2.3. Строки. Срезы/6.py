"""
Туда и обратно
"""

word = input()
if len(word) % 2 == 0:
    if word[:len(word) // 2] == word[:len(word) // 2 - 1:-1]:
        print('True')
    else:
        print('False')
else:
    if word[:len(word) // 2] == word[:len(word) // 2:-1]:
        print('True')
    else:
        print('False')
