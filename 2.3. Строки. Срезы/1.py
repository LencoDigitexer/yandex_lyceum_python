"""
Попарно
"""

name_letters = input()
for i in range(0, len(name_letters), 2):
    print(name_letters[i:i + 2])
    