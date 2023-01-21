"""
Медленнее
"""

word = input()
for i in range(len(word)):
    print(word[i] * (i + 1), end='')
