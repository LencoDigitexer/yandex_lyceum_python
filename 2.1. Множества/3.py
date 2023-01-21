"""
Общие буквы
"""

A = set(input())
B = set(input())
C = set(input())
for letter in (A & B) | (A & C) | (C & B):
    print(letter, end='')
