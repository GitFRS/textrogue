import os


def check_is_command():
    global cmd_usr
    global game_over
    if cmd_usr == '/help':
        for s in help_text:
            print(s)
    elif cmd_usr == '/new_game':
        print("\nВы уверены, что хотите начать новую игру? (y/n)")
        print("При начале новой игры весь ваш прогресс сбрасывается.\n")
        cmd_usr = input('>')
        if cmd_usr == 'y':
            print("\n%ПОКА ЧТО НЕ РАБОТАЕТ%\n")
        elif cmd_usr == 'n':
            print("\n%ПОКА ЧТО НЕ РАБОТАЕТ%\n")  # А должно ли?
    elif cmd_usr == '/settings':
        print("\n%ПОКА ЧТО НЕ РАБОТАЕТ%\n")
    elif cmd_usr == '/clear':                    # Разные аргументы в system в
        os.system("clear")                       # зависимости от платформы
    elif cmd_usr == '/save':
        print("\n%ПОКА ЧТО НЕ РАБОТАЕТ%\n")
    elif cmd_usr == '/exit':
        input("\nНажмите любую клавишу для выхода из игры...")
        game_over = True


def play():
    global game_over
    global main_text
    global cmd_usr
    cmd_usr = input('>')


cmd_usr = ''
game_over = False
main_text = ['%GAME NAME%\n\n\n', 'Для ввода команд напечатайте их\n',
             'на клавиатуре и нажмите Enter.\n',
             'Чтобы начать новую игру, введите /new_game\n']
help_text = ['\nСписок команд:\n\n',
             '/help    список команд\n',
             '/new_game    начать новую игру\n',
             '/settings    настройки\n',
             '/clear    очистить экран\n',
             '/save    сохранить игру\n',
             '/exit    выйти из игры\n']

for s in main_text:
    print(s)

while not game_over:
    play()
    check_is_command()
