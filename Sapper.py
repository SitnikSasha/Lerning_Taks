import random


def adder(i, j, mine_coord=[[1, 1]]) -> str:
    for k in mine_coord:
        if k[0] == i and k[1] == j:  # координаты мины совпадают с итератором
            return "!"  # значит будте мина
    return "0"  # иначе - пустая клетка


def mine_seeker(chek_field: list):
    for i in range(len(chek_field)):
        for j in range(len(chek_field[i])):
            # если клетка - мина
            if chek_field[i][j] == "!":
                continue
            # если клетка - один из углов поля
            elif i == 0 and j == 0:
                for y in range(2):
                    for x in range(2):
                        if chek_field[y][x] == "!":
                            chek_field[i][j] = int(chek_field[i][j]) + 1
                        else:
                            continue
            elif i == len(chek_field) - 1 and j == 0:
                mine_row = len(chek_field) - 2
                for y in range(2):
                    for x in range(2):
                        if chek_field[y+mine_row][x] == "!":
                            chek_field[i][j] = int(chek_field[i][j]) + 1
                        else:
                            continue
            elif j == len(chek_field[i]) - 1 and i == 0:
                mine_col = len(chek_field[0]) - 2
                for y in range(2):
                    for x in range(2):
                        if chek_field[y][x+mine_col] == "!":
                            chek_field[i][j] = int(chek_field[i][j]) + 1
                        else:
                            continue
            elif j == len(chek_field[i]) - 1 and i == len(chek_field) - 1:
                mine_col = len(chek_field[0]) - 2
                mine_row = len(chek_field) - 2
                for y in range(2):
                    for x in range(2):
                        if chek_field[y+mine_row][x+mine_col] == "!":
                            chek_field[i][j] = int(chek_field[i][j]) + 1
                        else:
                            continue
            # если клетка находится на гранях поля
            elif i == len(chek_field) - 1:
                mine_row = i - 1
                mine_col = j - 1
                for y in range(2):
                    for x in range(3):
                        if chek_field[y+mine_row][x+mine_col] == "!":
                            chek_field[i][j] = int(chek_field[i][j]) + 1
                        else:
                            continue
            elif j == len(chek_field[i]) - 1:
                mine_col = j - 1
                mine_row = i - 1
                for y in range(3):
                    for x in range(2):
                        if chek_field[y+mine_row][x+mine_col] == "!":
                            chek_field[i][j] = int(chek_field[i][j]) + 1
                        else:
                            continue
            elif j == 0:
                mine_row = i - 1
                for y in range(3):
                    for x in range(2):
                        if chek_field[y + mine_row][x] == "!":
                            chek_field[i][j] = int(chek_field[i][j]) + 1
                        else:
                            continue
            elif i == 0:
                mine_col = j - 1
                for y in range(2):
                    for x in range(3):
                        if chek_field[y][x + mine_col] == "!":
                            chek_field[i][j] = int(chek_field[i][j]) + 1
                        else:
                            continue
            # клетка где-то не на краях поля
            else:
                mine_col = j - 1
                mine_row = i - 1
                for y in range(3):
                    for x in range(3):
                        if chek_field[y+mine_row][x+mine_col] == "!":
                            chek_field[i][j] = int(chek_field[i][j]) + 1
                        else:
                            continue


def solver(n: int, m: int, mine_coord=[[1, 1]]):
    play_field = []
    for i in range(n):  # генерируем базовое поле с минами
        time_col = [adder(i, j, mine_coord) for j in range(m)]
        play_field.append(time_col)
    mine_seeker(play_field)  # определяем количество мин вокруг клеток-"не мин"
    for k in range(n):  # красивый вывод поля
        for k_1 in range(m):
            print(f'{play_field[k][k_1]}', end=' ')
        print()


def main():
    n = int(input('rows(n):'))  # количество рядом
    m = int(input('columns(m):'))  # кодичество элементов в ряду
    mines = int(input('mine number: '))  # количество мин(логично, но всё же, меншье чем n*m)
    if mines >= n*m:
        return print(f"A lot of mines, take less than rows*columns.")
    mine_coord = []
    for key in range(mines):  # генерируем координаты мин по их количеству и пределам поля
        mine = [random.randint(0, n-1), random.randint(0, m-1)]
        mine_coord.append(mine)
    solver(n, m, mine_coord)


if __name__ == '__main__':
    main()
