"""
Слово из букв
"""

answer_string = ''
for i in range(int(input())):
    word = input()
    if len(word) < i + 1:
        print('None')
        break
    answer_string += word[len(word) - i - 1]
    # answer_string += word[-1 - i] тоже правильно
else:
    print(answer_string)
