"""
Сэндвич
"""

word = input()
key_word = ''
left_string = right_string = ''
left_side = right_side = len(word) // 2
left_index = right_index = 0
if len(word) % 2 != 0:
    left_side += 1

for i in range(left_side):
    left_string += word[i]
for i in range(left_side, len(word)):
    right_string += word[i]

for i in range(len(word)):
    if i % 2 == 0:
        key_word += left_string[left_index]
        left_index += 1
    else:
        key_word += right_string[right_index]
        right_index += 1
print(key_word)
