suspicious_word = "подозрительный"
sentence_count = 0
while True:
    sentence = input().strip()
    if sentence.startswith(suspicious_word):
        break
    sentence_count += 1
    if sentence_count == 1:
        print(sentence.lower())
    elif sentence_count == 2:
        print(sentence.upper())
    elif sentence_count == 3:
        words = sentence.split()
        processed_words = [word.capitalize() for word in words]
        print(" ".join(processed_words))
        sentence_count = 0
