# колличество клеток
board_size = 3
# игровое поле
board = [1,2,3,
         4,5,6,
         7,8,9]

def draw_board():
    """Выводим игровое поле"""
    print("_" * 4 * board_size)
    for i in range(board_size):
        print((" " * 3 + "|")*3)
        print('', board[i*3], "|", board[1 + i*3], "|", board[2 + i*3], "|")
        print(("_" * 3 + "|") * 3)
def game_step(index, char):
    """Выполняем ход"""
    if index > 9 or board[index-1] in ["X", "O"]:
        return False
    board[index - 1] = char
    return True
def check_win():
    win = False

    win_combination = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
    )
    for pos in win_combination:
        if board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]:
            win = board[pos[0]]
    return win

def start_game():
    draw_board()
    # текущий игрок
    current_player = "X"
    # номер шага
    step = 1

    while (step < 10) and (check_win() == False):

        index = input(f"Ходит игрок {current_player}. Введите номер поля (0 - выход из игры):")
        if index == "0":
            print("Вы завершили игру!")
            break

        # если получилось сделать шаг
        if game_step(int(index), current_player):
            draw_board()
            print("Удачный ход")
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
            step += 1

        else:
            print("Неверный номер, повторите!")
    if step > 9 and index != "0":
        print("Игра окончена, ничья!")
    elif 1 <= step <= 8 and index != "0":
        print("Выиграл " + (check_win()))


print("Добро пожаловать в крестики-нолики!")

start_game()