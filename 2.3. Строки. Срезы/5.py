"""
До и после
"""

word_to_flip = input()
flip_index = 0
for i in word_to_flip:
    if i == '-':
        break
    flip_index += 1
#  print(word_to_flip[flip_index])
print(word_to_flip[flip_index + 1:] + '-' + word_to_flip[:flip_index])
