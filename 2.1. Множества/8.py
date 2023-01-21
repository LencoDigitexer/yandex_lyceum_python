"""
Антиматерия
"""

num = input()
only_original_result_set = set()
already_deleted = set()
current_set = set()
while num:
    if num == '-1':  # Достигли конца сосуда. Начинаем разбираться
        for elem in current_set:
            if elem not in only_original_result_set and elem not in already_deleted:
                only_original_result_set.add(elem)
            else:
                only_original_result_set.discard(elem)
                already_deleted.add(elem)
        current_set.clear()  # для следующего сосуда
    else:
        current_set.add(num)  # набираем текущий сосуд
    num = input()
print(*only_original_result_set)
