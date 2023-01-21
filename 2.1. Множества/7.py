"""
Палитра
"""

all_colors = set()
repeated_colors = set()
all_repeats_amount = 0
for i in range(int(input())):
    colors = int(input())
    for j in range(colors):
        color = input()
        if color in all_colors:
            if color in repeated_colors:
                all_repeats_amount += 1
            else:
                all_repeats_amount += 2
                repeated_colors.add(color)
        else:
            all_colors.add(color)
print(len(repeated_colors), all_repeats_amount)
