n = int(input())
m = int(input())
res = set()
for i in range(n):
    k = int(input())
    s = input()
    result_set = s[:m:k]
    res.add(result_set)
print(res)
for i in res:
    print(i)