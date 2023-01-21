"""
Ссылки на источник
"""

line = input()
open_bracket_pos = close_bracket_pos = 0

while '[' in line:
    for i in range(len(line)):
        if line[i] == '[':
            open_bracket_pos = i
        elif line[i] == ']':
            close_bracket_pos = i
            line = line[:open_bracket_pos] + line[close_bracket_pos + 1:]
            # print(line)
            break
print(line)
