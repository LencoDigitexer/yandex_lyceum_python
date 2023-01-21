"""
Без повторений
"""

word = input()
word_set = set(word)
while word:
    if len(word) == len(word_set):
        print(word)
    word = input()
    word_set = set(word)
