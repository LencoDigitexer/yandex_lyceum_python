"""
Слова
"""

string = input()
for char in string:
    if char == ' ' or char == '\n':
        print()
    else:
        print(char, end='')
