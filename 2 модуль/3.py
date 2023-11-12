n = int(input())
for i in range(n):
    set1 = set(map(int, input().split()))
    set2 = set(map(int, input().split()))
    result_set = sorted([x for x in set1 if x % 3 != 0 and x not in set2], reverse=True)
    if result_set:
        print(': '.join(map(str, result_set)))
    else:
        print()
    result_set2 = sorted([x for x in set1 if x % 3 != 0 and x not in set2 and x not in result_set], reverse=True)
    if result_set2:
        print(': '.join(map(str, result_set2)))
    else:
        pass
