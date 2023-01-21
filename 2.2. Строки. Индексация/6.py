"""
Серединка
"""

s = input()
s_length = len(s)
print(s[s_length // 2 - (s_length + 1) % 2])
