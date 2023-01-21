"""
Следующие три
"""

number = int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(4):
    print(alphabet[(number + i - 1) % 26], end='')
