import time
import random

tic = time.perf_counter()
M = 9


def print_solved(a):
    for i in range(M):
        if i == 3 or i == 6:
            for k in range(M):
                print('-', end=' ')
            print()
        for j in range(M):
            if j == 2 or j == 5:
                print(f'{a[i][j]}|', end="")
            else:
                print(a[i][j], end=" ")
        print()


def solve(ground, row, col, num):
    for x in range(9):  # Есть ли в строке
        if ground[row][x] == num:
            return False

    for x in range(9):  # Есть ли в столбце
        if ground[x][col] == num:
            return False
    # Определяем подзону 3х3
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):  # Есть ли в подзоне 3х3
        for j in range(3):
            if ground[i + start_row][j + start_col] == num:
                return False
    return True
# seeking same number in row and column


def sudoku(ground, row, col):
    if row == M - 1 and col == M:
        return True
    if col == M:
        row += 1
        col = 0
    if ground[row][col] > 0:
        return sudoku(ground, row, col + 1)
    for i in range(9):
        num = random.randint(1, 9)
        if solve(ground, row, col, num):
            ground[row][col] = num
            if sudoku(ground, row, col + 1):
                return True
        ground[row][col] = 0
    return False
# sudoku solver main part


def task_active():
    test_ground = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    if sudoku(test_ground, 0, 0):
       print_solved(test_ground)
       toc = time.perf_counter()
       print(f'\nsolution time: {toc-tic} sec')

    else:
        print('Solution error.')


if __name__ == '__main__':
    task_active()