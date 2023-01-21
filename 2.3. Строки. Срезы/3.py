"""
Дровосек
"""

word_to_cut = input()
step = int(input())
while len(word_to_cut) >= step:
    print(word_to_cut[len(word_to_cut) - step:len(word_to_cut)])
    word_to_cut = word_to_cut[0:len(word_to_cut) - step]
    print(word_to_cut[0:step])
    word_to_cut = word_to_cut[step:len(word_to_cut)]
else:
    print(word_to_cut)
