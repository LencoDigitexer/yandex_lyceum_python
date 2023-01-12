"""
Поле чудес
"""

dir = 1j
pos = complex()
while True:
    move = input()
    match move:
        case 'СТОП':
            break
        case 'налево':
            dir *= 1j
        case 'направо':
            dir /= 1j
        case 'шаг':
            pos += dir
            
print(int(pos.real), int(pos.imag))
