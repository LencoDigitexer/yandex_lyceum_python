words_1 = input().split()
words_2 = input().split('#')
words_3 = input().split('+++')

for word in words_1:
    # выбираем из второй строки слова, длина которых не меньше проверяемого слова и количество различных букв в нем не меньше 4
    words_2_filtered = [w for w in words_2 if len(w) >= len(word) and len(set(w)) >= 4]
    # из третьей строки выбираем слова, в которых есть прописные буквы или цифры и есть как минимум две буквы, которых нет в проверяемом слове
    words_3_filtered = [w for w in words_3 if (any(c.isupper() or c.isdigit() for c in w) and 
                                                len(set(w.lower()) - set(word.lower())) >= 2)]
    # форматируем вывод
    print(f"{word}:")
    if words_2_filtered:
        words_2_str = ', '.join(words_2_filtered)
        words_2_str = ' '.join([w.capitalize() if w.lower() != word.lower() else w for w in words_2_str.split()])
        print(words_2_str)
    else:
        print()
    if words_3_filtered:
        words_3_str = ' '.join([w[:-1] + word[-1].upper() + ' ' for w in words_3_filtered])
        print(words_3_str)
    else:
        print()
