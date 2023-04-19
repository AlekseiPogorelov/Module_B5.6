# Приветствие
def greeting():
    print("-------------------------")
    print("     Крестики-нолики     ")
    print("-------------------------")
    print("  Игрок1 - X; Игрок2 - 0 ")
    print("-------------------------")
    print("вводите координаты: a b  ")
    print("      через пробел       ")
    print(" a - строка; b - столбец ")

# Игровое поле
def playing_field():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  _______________ ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

# Запрс координат
def request():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue
        a, b = cords
        if not (a.isdigit()) or not (b.isdigit()):
            print(" Введите числа! ")
            continue
        a, b = int(a), int(b)
        if 0 > a or a > 2 or 0 > b or b > 2:
            print(" Координаты вне диапазона! ")
            continue
        if field[a][b] != " ":
            print(" Клетка занята! ")
            continue
        return a, b

# Определение победителя
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for d in cord:
            symbols.append(field[d[0]][d[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Игрок1!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл Игрок2!")
            return True
    return False

greeting()
field = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    playing_field()
    if count % 2 == 1:
        print(" Ходит Игрок1!")
    else:
        print(" Ходит Игрок2!")

    a, b = request()

    if count % 2 == 1:
        field[a][b] = "X"
    else:
       field[a][b] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break