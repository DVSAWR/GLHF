'''

D. Слоны и ладьи
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
На шахматной доске стоят слоны и ладьи, необходимо посчитать, сколько клеток не бьется ни одной из фигур.

Шахматная доска имеет размеры 8 на 8. Ладья бьет все клетки горизонтали и вертикали, проходящих через клетку, где она
стоит, до первой встретившейся фигуры. Слон бьет все клетки обеих диагоналей, проходящих через клетку, где он стоит,
до первой встретившейся фигуры.

Формат ввода
В первых восьми строках ввода описывается шахматная доска. Первые восемь символов каждой из этих строк описывают
состояние соответствующей горизонтали: символ B (заглавная латинская буква) означает, что в клетке стоит слон,
символ R — ладья, символ * — что клетка пуста. После описания горизонтали в строке могут идти пробелы, однако
длина каждой строки не превышает 250 символов. После описания доски в файле могут быть пустые строки.

Формат вывода
Выведите количество пустых клеток, которые не бьются ни одной из фигур.

Пример 1
Ввод
********
********
*R******
********
********
********
********
********
Вывод
49
Пример 2
Ввод
********
********
******B*
********
********
********
********
********
Вывод
54
Пример 3
Ввод
********
*R******
********
*****B**
********
********
********
********
Вывод
40

'''

BOARD = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]

print(BOARD)

print('---')
for i in BOARD:
    print(i)

print('---INPUT----')

# BOARD = []
#
# for i in range(8):
#     BOARD.append(tuple(input()[0:8]))
#
# for i in BOARD:
#     print(i)


print('\n---SOLUTION TRY---')

BOARD = [
    ('*', '1', '*', '*', '*', '*', '*', '*'),  # 1
    ('*', '2', '*', '*', '*', '*', '*', '*'),  # 2
    ('1', 'R', '3', '4', '5', '6', '7', '8'),  # 3
    ('*', '4', '*', '*', '*', '*', '*', '*'),  # 4
    ('*', '5', '*', '*', '*', '*', '*', '*'),  # 5
    ('*', '6', '*', '*', '*', '*', '*', '*'),  # 6
    ('*', '7', '*', '*', '*', '*', '*', '*'),  # 7
    ('*', '8', '*', '*', '*', '*', '*', '*'),  # 8
]

print(BOARD)

total_board_cells = 64
empty_cells = 0

r_cells = 0
b_cells = 0

# R = Rock - горизонтлальные и вертикальные клетки
# B = Bishop - диагональные клетки

# # R cells
# for i in BOARD:
#     r_cells_count_in_line = i.count('R')
#     b_cells_count_in_line = i.count('B')
#     print(f'R: {r_cells_count_in_line}   B: {b_cells_count_in_line}')
#
#     r_cells += r_cells_count_in_line
#     b_cells += b_cells_count_in_line
#
# print(f'SUM > R: {r_cells}   B: {b_cells}')
#
# # Количество пустых клеток с фигурами
# print(f'EMPTY CELLS EMPTY BOARD: {total_board_cells}')
#
# empty_cells_with_figures = total_board_cells - r_cells - b_cells
# print(f'EMPTY CELLS WITH FIGURES: {empty_cells_with_figures}')

# Индексы R в ряду
print('')
r_cells = 0
b_cells = 0

for i in BOARD:
    print(i)

for line_index, line in enumerate(BOARD):
    for item_index, item in enumerate(line):
        if item == 'R':
            print(f'line: {line_index} item: {item} item_index: {item_index}')
            r_cells += 1

        elif item == 'B':
            print(f'line: {line_index} item: {item} item_index: {item_index}')
            b_cells += 1

        else:
            pass

print('-----R and B indexes-----')
r_cells = 0
b_cells = 0

for i in BOARD:
    print(i)

for line_index, line in enumerate(BOARD):
    for item_index, item in enumerate(line):
        if item == 'R':
            print(f'line: {line_index} item: {item} item_index: {item_index}')
            r_cells += 1


        elif item == 'B':
            print(f'line: {line_index} item: {item} item_index: {item_index}')
            b_cells += 1

        else:
            pass

print('---directions of R---')
# line: 2 item: R item_index: 1
r_item = 'R'
r_item_index = 1
r_item_line_index = 2

r_left = []
r_right = []
r_top = []
r_bottom = []

for i in BOARD[r_item_line_index][0:r_item_index]:
    r_left.append(i)
print(r_left)

for i in BOARD[r_item_line_index][r_item_index + 1:]:
    r_right.append(i)
print(r_right)

for i in BOARD[0:r_item_line_index]:
    r_top.append(i[r_item_index])
print(r_top)

for i in BOARD[r_item_line_index + 1:]:
    r_bottom.append(i[r_item_index])
print(r_bottom)

print('---reversed directions of R---')

r_left.reverse()
print(r_left)

print(r_right)

r_top.reverse()
print(r_top)

print(r_bottom)

print('---cut directions---')

cut_r_left = []
cut_r_right = []
cut_r_top = []
cut_r_bottom = []

for cut_index, i in enumerate(r_left):
    if i == 'R' or i == 'B':
        cut_r_left = r_left[:cut_index]
        break
    else:
        cut_r_left = r_left

for cut_index, i in enumerate(r_right):
    if i == 'R' or i == 'B':
        cut_r_right = r_right[:cut_index]
        break
    else:
        cut_r_right = r_right

for cut_index, i in enumerate(r_top):
    if i == 'R' or i == 'B':
        cut_r_top = r_top[:cut_index]
        break
    else:
        cut_r_top = r_top

for cut_index, i in enumerate(r_bottom):
    if i == 'R' or i == 'B':
        cut_r_bottom = r_bottom[:cut_index]
        break
    else:
        cut_r_bottom = r_bottom

print(cut_r_left)
print(cut_r_right)
print(cut_r_top)
print(cut_r_bottom)

print('--SUM of empty R cut cells--')

print(r_cells)
x = len(cut_r_left) + len(cut_r_right) + len(cut_r_top) + len(cut_r_bottom)
print(x)
print(total_board_cells - x - r_cells)

print('----def directions of R-----')


def r_empty_cells(r_item_index, r_item_line_index):
    r_left = []
    r_right = []
    r_top = []
    r_bottom = []
    cut_r_left = []
    cut_r_right = []
    cut_r_top = []
    cut_r_bottom = []

    for i in BOARD[r_item_line_index][0:r_item_index]:
        r_left.append(i)

    for i in BOARD[r_item_line_index][r_item_index + 1:]:
        r_right.append(i)

    for i in BOARD[0:r_item_line_index]:
        r_top.append(i[r_item_index])

    for i in BOARD[r_item_line_index + 1:]:
        r_bottom.append(i[r_item_index])

    r_left.reverse()
    r_top.reverse()

    for cut_index, i in enumerate(r_left):
        if i == 'R' or i == 'B':
            cut_r_left = r_left[:cut_index]
            break
        else:
            cut_r_left = r_left

    for cut_index, i in enumerate(r_right):
        if i == 'R' or i == 'B':
            cut_r_right = r_right[:cut_index]
            break
        else:
            cut_r_right = r_right

    for cut_index, i in enumerate(r_top):
        if i == 'R' or i == 'B':
            cut_r_top = r_top[:cut_index]
            break
        else:
            cut_r_top = r_top

    for cut_index, i in enumerate(r_bottom):
        if i == 'R' or i == 'B':
            cut_r_bottom = r_bottom[:cut_index]
            break
        else:
            cut_r_bottom = r_bottom

    print(cut_r_left, cut_r_right, cut_r_top, cut_r_bottom)  # FOR DELETE

    return len(cut_r_left) + len(cut_r_right) + len(cut_r_top) + len(cut_r_bottom)


r_empty_cells(1, 2)

print('-----SMTH-----')
BOARD = [
    ['*', '1', '*', '*', '*', '*', '*', '*'],  # 1
    ['*', '2', '*', '*', '*', '*', '*', '*'],  # 2
    ['1', 'R', '3', '4', '5', '6', '7', '8'],  # 3
    ['*', '4', '*', '*', '*', '*', '*', '*'],  # 4
    ['*', '5', '*', '*', '*', '*', '*', '*'],  # 5
    ['*', '6', '*', '*', '*', '*', '*', '*'],  # 6
    ['*', '7', '*', '*', '*', '*', '*', '*'],  # 7
    ['*', '8', '*', '*', '*', '*', '*', '*'],  # 8
]

r_cells = 0

for i in BOARD:
    print(i)

for line_index, line in enumerate(BOARD):
    for item_index, item in enumerate(line):
        if item == 'R':
            print(f'line: {line_index} item: {item} item_index: {item_index}')
            r_cells += r_empty_cells(int(item_index), int(line_index)) + 1

print(r_cells)

print('\n\n\n\n\n-----dict??------\n')

# ********
# ********
# *R******
# ********
# ********
# ********
# ********
# ********


# a b c d e f g h
# 1 2 3 4 5 6 7 8

klst = []

for i in 'a b c d e f g h'.split():
    for k in range(8):
        klst.append(i + str(k + 1))


def show_board():
    count = 0
    for k, v in BOARD.items():
        if count % 8 == 0:
            print('')
        count += 1
        print(k, v, end=' ')
    print('')


# vstr = input()[0:8] + input()[0:8] + input()[0:8] + input()[0:8] + input()[0:8] + input()[0:8] + input()[0:8] + input()[0:8]
# print(strinp)
vstr = ('********'
        '********'
        '*R******'
        '********'
        '********'
        '********'
        '********'
        '********')

BOARD = {k: v for k, v in zip(klst, vstr)}

show_board()

print('\n---directions of R in dict-enumerate()?--')

ENUMERATE_BOARD = enumerate(BOARD)


def show_board2():
    count = 0
    for k, v in ENUMERATE_BOARD:
        if count % 8 == 0:
            print('')
        count += 1
        print(f'{k, v}', end=' ')
    print('')


show_board2()

print('\n\n----dict with int keys ???----')

# vstr = input()[0:8] + input()[0:8] + input()[0:8] + input()[0:8] + input()[0:8] + input()[0:8] + input()[0:8] + input()[0:8]
# print(strinp)
vstr = ('********'
        '********'
        '*R******'
        '********'
        '********'
        '********'
        '********'
        '********')

klst = list(range(64))

BOARD = {k: v for k, v in zip(klst, vstr)}


def show_board():
    count = 0
    for k, v in BOARD.items():
        if count % 8 == 0:
            print('')
        count += 1
        print(k, v, end=' ')
    print('')


show_board()

for k, v in BOARD.items():
    if v == 'R':
        print(f'FOR VALUE: {v} KEY: {k}')

print('\n\n\n-------list of dicts??------')

BOARD = []

# vstr = input()[0:8], input()[0:8], input()[0:8] + input()[0:8] + input()[0:8] + input()[0:8] + input()[0:8] + input()[0:8]
# print(strinp)
vline = ('********',
         '********',
         '*R******',
         '********',
         '********',
         '********',
         '********',
         '********')

print(vline)

for i in vline:
    BOARD.append({k: v for k, v in zip(range(len(i)), i)})

print(BOARD)

def show_board():
    print('list of dicts')
    for l, d in enumerate(BOARD):
        print(f'line {l}: {d}')


show_board()



print('\n----directions of R-----')

for l, d in enumerate(BOARD):
    for k, v in d.items():
        if v == 'R':
            print(f'line: {l} key: {k} value: {v}')
        
