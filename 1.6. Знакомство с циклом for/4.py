"""
Глиссада
"""

start = int(input())
steps = int(input())
end = int(input())

for i in range(start, end - 1, -steps):
    print("Высота " + str(i))

print("Глиссада")
