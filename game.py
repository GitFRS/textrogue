
def show_screen(screen):
    for i in range(height + 1):
        for j in range(width):
            print(screen[i][j], end='')
        print()

height = 30
width = 100
screen = []
for i in range(30):
    for j in range(100):
        if i == 0:
             screen.append('-' * 100)
             break
        elif i == 1:
             screen.append('|' + '1. Новая игра' + ' ' * 85 + '|')
             break
        elif i == 2:
            screen.append('|' + '2. Продолжить игру' + ' ' * 80 + '|')
            break
        elif i == 3:
            screen.append('|' + '3. Настройки' + ' ' * 86 + '|')
            break
        elif i == 4:
            screen.append('|' + '4. Выход' + ' ' * 90 + '|')
            break
    if i not in (0, 1, 2, 3, 4, 99):
        screen.append('|' + ' ' * 98 + '|')
screen.append('-' * 100)
show_screen(screen)

#TODO: Необходимо сделать ввод команд пользователем после строки "4. Выход".
#      Чтобы указать пользователю, что можно что-то вводить, можно использовать '>>>'
