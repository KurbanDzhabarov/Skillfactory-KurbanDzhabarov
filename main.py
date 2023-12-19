# карта
maps = [1,2,3,
        4,5,6,
        7,8,9,]

# победные линии
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

def print_maps(): # функция выводит карту на экран
    print(maps[0], end = " ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])

def step_maps(step,symbol): # функция хода в ячейку(step), symbol(X или O)
    ind = maps.index(step)
    maps[ind] = symbol


def get_result(): # Получить текущий результат игры. Эта функция вернет «X» в случае победы крестиков и «O» в случае победы ноликов.
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win


# Основная программа
game_over = False
player1 = True
counter = 0
while game_over == False:

    # 1. Показываем карту
    print_maps()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Человек 1, ваш ход: "))
        counter += 1
    else:
        symbol = "O"
        step = int(input("Человек 2, ваш ход: "))
        counter += 1

    step_maps(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False
    if counter == 9 and win not in ["X", "O"]:
        game_over = True
        win = "Ничья!"

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_maps()
print("Победил", win)