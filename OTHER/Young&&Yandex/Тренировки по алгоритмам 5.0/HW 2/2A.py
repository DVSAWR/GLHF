'''

На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник, со сторонами, параллельными линиям сетки, покрывающий все закрашенные клетки.

Формат ввода
Во входном файле, на первой строке, находится число K (1 ≤ K ≤ 100). На следующих K строках находятся пары чисел Xi и Yi — координаты закрашенных клеток (|Xi|, |Yi| ≤ 109).

Формат вывода
Выведите в выходной файл координаты левого нижнего и правого верхнего углов прямоугольника.

Пример
Ввод
4
1 3
3 1
3 5
6 3

Вывод
1 1 6 5

'''


print('------XXXXXX-------')

# min x min y max x max y

K = 1
coords = []

for i in range(K):
    coords.append(tuple(map(int, input().split())))

print(list(coords))


minx = coords[0][0]
miny = coords[0][1]

maxx = coords[0][0]
maxy = coords[0][1]

for i in coords:
    # print(i[0], i[1])
    # для X
    if i[0] < minx:
        minx = i[0]
    if i[0] > maxx:
        maxx = i[0]

    # для Y
    if i[1] < miny:
        miny = i[1]
    if i[1] > maxy:
        maxy = i[1]

print(f'X Y MIN: {minx} {miny}\nX Y MAX: {maxx} {maxy}')


print('--------------DONE--------------')

K = int(input())
coords = []

for i in range(K):
    coords.append(tuple(map(int, input().split())))

minx = coords[0][0]
miny = coords[0][1]
maxx = coords[0][0]
maxy = coords[0][1]

for i in coords:
    if i[0] < minx:
        minx = i[0]
    if i[0] > maxx:
        maxx = i[0]
    if i[1] < miny:
        miny = i[1]
    if i[1] > maxy:
        maxy = i[1]

print(minx, miny, maxx, maxy)
