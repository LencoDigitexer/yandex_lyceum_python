"""
Сравнение строк (not work in yandex)
"""


def solution(first, second, third):
    minimum = min(first, second, third, key=len)

    n = 1 * ((len(minimum) == len(first)) and (minimum != first) and
             (first <= minimum)) or\
        2 * ((len(minimum) == len(second)) and (minimum != second) and
             (second <= minimum)) or\
        3 * ((len(minimum) == len(third)) and (minimum != third) and
             (third <= minimum))

    return first * (n == 1) + second * (n == 2) + third * (n == 3) or minimum


print(len(solution(input(), input(), input())))
