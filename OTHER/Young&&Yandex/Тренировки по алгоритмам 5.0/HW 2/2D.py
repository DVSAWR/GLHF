'''

Из шахматной доски по границам клеток выпилили связную (не распадающуюся на части) фигуру без дыр. Требуется определить ее периметр.

Формат ввода
Сначала вводится число N (1 ≤ N ≤ 64) – количество выпиленных клеток. В следующих N строках вводятся координаты выпиленных клеток, разделенные пробелом (номер строки и столбца – числа от 1 до 8). Каждая выпиленная клетка указывается один раз.

Формат вывода
Выведите одно число – периметр выпиленной фигуры (сторона клетки равна единице).

Пример 1
Ввод
3
1 1
1 2
2 1

Вывод
8

Пример 2
Ввод
1
8 8

Вывод
4

'''

# BOARD CREATE

board = []
line_board = 'o ' * 8
for i in range(8):
    board.append(line_board.split())

for i in board:
    print(i)

print('\n')
print(board)

print('\n\n-------------SOLVE-------\n')

# INPUT
# n = 3  # CELLS COUNT
# coords = [(1, 1), (1, 2), (2, 1)]

# n = 16
# coords = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]

n = 1
coords = [(8, 7), (7, 8), (8, 8), (7, 7)]  # (5, 8), (6, 8), (7, 7),

# n = 7
# coords = [(5, 1), (5, 3), (6, 4), (6, 5), (7, 5), (6, 3), (5, 2)]

for i in coords:
    board[i[1] - 1][i[0] - 1] = 4

# SHOW CELLS RECOUNT
for line in board:
    print('')
    for v in range(8):
        print(line[v], end=' ')
print('')

# CELLS RECOUNT
for line in range(8):
    for cell in range(8):
        if cell != 7 and type(board[line][cell]) == int and type(board[line][cell + 1]) == int:  # RIGHT
            board[line][cell] -= 1
            board[line][cell + 1] -= 1
        if line != 7 and type(board[line][cell]) == int and type(board[line + 1][cell]) == int:  # TOP
            board[line][cell] -= 1
            board[line + 1][cell] -= 1


# SHOW CELLS RECOUNT 2
for line in board:
    print('')
    for v in range(8):
        print(line[v], end=' ')
print('\n')

# SHOW ANSWER
cells_count = 0
for line in board:
    for v in line:
        if type(v) == int:
            cells_count += v

print(f'ANSWER: {cells_count}')

print('---------------DONE--------------\n')

n = int(input())
coords = []
for i in range(n):
    coords.append(tuple(map(int, input().split())))

board = []
line_board = 'o ' * 8
for i in range(8):
    board.append(line_board.split())

for i in coords:
    board[i[1] - 1][i[0] - 1] = 4

for line in range(8):
    for cell in range(8):
        if cell != 7 and type(board[line][cell]) == int and type(board[line][cell + 1]) == int:  # RIGHT
            board[line][cell] -= 1
            board[line][cell + 1] -= 1
        if line != 7 and type(board[line][cell]) == int and type(board[line + 1][cell]) == int:  # TOP
            board[line][cell] -= 1
            board[line + 1][cell] -= 1

cells_count = 0
for line in board:
    for v in line:
        if type(v) == int:
            cells_count += v

print(cells_count)
