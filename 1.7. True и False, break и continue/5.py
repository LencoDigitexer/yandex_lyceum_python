"""
Сравнение строк
"""


def bu_bu(s_L, s_R):
    return len(s_L) <= len(s_R) and s_L <= s_R


a = input()
b = input()
c = input()

lis = [a, b, c]

n = 4 * bu_bu(lis[0], lis[1]) + 2 * bu_bu(lis[0], lis[2]) + bu_bu(
    lis[1], lis[2])
res = lis[0] * (n > 5) + lis[1] * ((n < 5) and
                                   (n % 2)) + lis[2] * ((n < 5) and
                                                        (n % 2 == 0))
print(len(res))
