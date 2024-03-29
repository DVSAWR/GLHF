'''

Дан массив из
N
 целых чисел. Все числа от
−
1
0
9
 до
1
0
9
.
Нужно уметь отвечать на запросы вида “Cколько чисел имеют значения от
L
 до
R
?”.

Формат ввода
Число
N
 (
1
≤
N
≤
1
0
5
). Далее
N
 целых чисел.
Затем число запросов
K
 (
1
≤
K
≤
1
0
5
).
Далее
K
 пар чисел
L
,
R
 (
−
1
0
9
≤
L
≤
R
≤
1
0
9
) — собственно запросы.

Формат вывода
Выведите
K
 чисел — ответы на запросы.
Пример
Ввод
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2

Вывод
5 2 2 0

'''

print('\n-------DONE-------\n')


# 1
# 1
# 3
# 1 1
#
# -1000000000 -1000000000
# 1000000000 1000000000


# 5
# 10 1 10 3 4
# 4
# 1 10
# 2 9
# 3 4
# 2 2

# 5 2 2 0

# def count_nums(array, l, r):
#     count = 0
#     for i in array:
#         if l <= i <= r:
#             count += 1
#     return count
#
#
# # n = int(input())
# # array = list(map(int, input().split()))
# # k = int(input())
#
# n = 5
# array = list(map(int, '10 1 10 3 4'.split()))
# k = 4
#
# answer = []
#
# for i in range(k):
#     l, r = map(int, input().split())
#     answer.append(count_nums(array, l, r))
#
# print(*answer)


# 5
# 10 1 10 3 4
# 4
# 1 10
# 2 9
# 3 4
# 2 2

# 5 2 2 0

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l


print('-----DONE-----')

from bisect import bisect_left, bisect_right
from collections import Counter

n = int(input())
array = list(map(int, input().split()))
array.sort()

counter = Counter(array)

k = int(input())
answer = []

for _ in range(k):
    l, r = map(int, input().split())
    left_index = bisect_left(array, l)
    right_index = bisect_right(array, r)
    count = right_index - left_index
    answer.append(count)

print(*answer)

# Первым шагом мы импортируем функции bisect_left и bisect_right из модуля bisect.
#
# bisect_left(arr, x) находит точное место, куда можно вставить x в отсортированный массив arr без изменения порядка элементов.
# bisect_right(arr, x) находит точное место после последнего вхождения x в отсортированный массив arr.
# Мы определяем массив array и сортируем его.
#
# Мы устанавливаем переменную k равной 1, чтобы выполнить этот код один раз.
#
# Мы устанавливаем значения l и r равными 1 и 10 соответственно.
#
# Затем мы используем bisect_left для нахождения индекса элемента, который больше или равен l. Этот индекс будет указывать на первое вхождение элемента, о котором мы хотим найти.
#
# После этого мы используем bisect_right для нахождения индекса элемента, который больше r. Это даст нам индекс, который указывает на первое вхождение элемента, большего, чем r, что позволит нам вычислить количество элементов, находящихся между l и r.
#
# Наконец, мы вычисляем количество элементов между l и r путем вычитания left_index из right_index.
#
# Таким образом, этот код использует бинарный поиск с помощью функций bisect_left и bisect_right, чтобы найти количество элементов в отсортированном массиве array, которые находятся между l и r.

print('------yandex------')

def binsearch(a, val):
    l = 0
    r = len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] >= val:
            r = m
        else:
            l = m + 1
    return l

n = int(input())
a = list(map(int, input().split()))
a.sort()
a.append(10**9 + 1)
k = int(input())
ans = []
for i in range(k):
    mn, mx = map(int, input().split())
    posmn = binsearch(a, mn)
    posmx = binsearch(a, mx + 1)
    ans.append(posmx - posmn)

print(*ans)
