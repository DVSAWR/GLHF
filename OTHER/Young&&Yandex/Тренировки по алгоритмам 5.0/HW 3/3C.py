'''


Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дан массив
a
 из
n
 чисел. Найдите минимальное количество чисел, после удаления которых попарная разность оставшихся чисел по модулю не будет превышать
1
, то есть после удаления ни одно число не должно отличаться от какого-либо другого более чем на
1
.
Формат ввода
Первая строка содержит одно целое число
n
 (
1
≤
n
≤
2
⋅
1
0
5
) — количество элементов массива
a
.
Вторая строка содержит
n
 целых чисел
a
1
,
a
2
,
…
,
a
n
 (
0
≤
a
i
≤
1
0
5
) — элементы массива
a
.

Формат вывода
Выведите одно число — ответ на задачу.
Пример 1
Ввод	Вывод
5
1 2 3 4 5
3
Пример 2
Ввод	Вывод
10
1 1 2 3 5 5 2 2 1 5
4

'''

print('\n----DONE-----\n')

from itertools import pairwise

# n = int(input())
# a = list(map(int, input().split()))

# n = 10
# a = [1, 1, 2, 3, 5, 5, 2, 2, 1, 5]

# n = 5
# a = [1, 2, 3, 4, 5]

# n = 10
# a = [1, 1, 2, 2, 2, 1, 2, 2, 1, 3]

n = 1
a = [33292]

print(a)

d = {}

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

nums = sorted(d.keys())

print(nums)

n_nums = len(nums)

answer = 0

if n_nums < 2:
    print(0)
else:
    for i in range(len(nums) - 1):
        if abs(nums[i] - nums[i + 1]) <= 1:
            answer = max(d[nums[i]] + d[nums[i + 1]], answer)
            print(max(d[nums[i]] + d[nums[i + 1]], answer))
    print('\nANSWER:')
    print(n - answer)

# for first, second in pairwise(nums):
#     if abs(first - second) <= 1:
#         answer = max(d[first] + d[second], answer)
#
# print(n - answer)

# from collections import Counter
# from itertools import pairwise
#
#
# def min_to_delete(a: list[int]) -> int:
#     counter = Counter(a)
#     unique_nums = sorted(counter.keys())
#     if len(unique_nums) < 2:
#         return 0
#     max_len = 1
#     for x, y in pairwise(unique_nums):
#         if abs(x - y) <= 1:
#             max_len = max(counter[x] + counter[y], max_len)
#     return len(a) - max_len
#
#
# if __name__ == '__main__':
#     n = int(input())
#     a = [int(s) for s in input().split()]
#     print(min_to_delete(a))


print('-----yandex-----')
