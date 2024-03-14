'''

На столе лежали две одинаковые верёвочки целой положительной длины.

Петя разрезал одну из верёвочек на N частей, каждая из которых имеет целую положительную длину, так что на столе стало N+1 верёвочек. Затем в комнату зашла Маша и взяла одну из лежащих на столе верёвочек. По длинам оставшихся на столе N верёвочек определите, какую наименьшую длину может иметь верёвочка, взятая Машей.

Формат ввода
Первая строка входных данных содержит одно целое число N — количество верёвочек, оставшихся на столе (2 ≤ N ≤ 1000). Во второй строке содержится N целых чисел li — длины верёвочек (1 ≤ li ≤ 1000).

Формат вывода
Выведите одно целое число — наименьшую длину, которую может иметь верёвочка, взятая Машей.

Пример 1
Ввод
4
1 5 2 1
Вывод
1
Пример 2
Ввод
4
5 12 4 3
Вывод
24

'''


print('\n-------------------')


n = 3
ropes = [3, 4, 5]

n = 200
mystr = '5 4 1 5 3 3 2 2 5 2 3 1 5 1 2 5 1 4 2 1 1 4 5 3 3 2 5 5 2 3 5 3 5 2 4 636 5 1 5 1 1 5 4 1 3 4 4 3 5 1 1 2 4 5 4 4 2 2 3 1 4 4 1 1 4 5 2 3 4 2 4 5 4 1 3 5 2 2 4 4 2 4 5 1 1 5 2 5 5 5 2 1 2 4 2 5 1 4 1 4 5 4 2 1 4 3 4 5 1 5 5 5 3 4 4 2 4 5 5 4 3 3 4 2 3 2 4 3 5 3 3 4 4 4 1 2 5 2 3 1 2 5 5 4 4 4 4 5 4 1 5 3 1 2 5 1 2 1 1 4 5 4 5 3 1 4 2 4 2 1 1 5 3 1 3 5 3 1 2 5 1 1 4 3 1 4 1 5 4 3 4 2 5 3 5 5 5 5 3 5'
ropes = list(map(int, mystr.split()))

print(n)
print(ropes)

sum_ropes = 0
max_rope = 0

for i in ropes:
    sum_ropes += i
    if i > max_rope:
        max_rope = i

sum_ropes_total = sum_ropes - max_rope

print('ROPE SUM:', sum_ropes)
print('MAX ROPE:', max_rope)

print('TOTAL ROPES SUM:', sum_ropes_total)


print('\nANSWER:', end=' ')
if max_rope > sum_ropes_total:
    print(max_rope - sum_ropes_total)
else:
    print(sum_ropes)
# elif max_rope == sum_ropes_total:
#     print(sum_ropes)




print('\n---DONE----')

n = int(input())
ropes = list(map(int, input().split()))

sum_ropes = 0
max_rope = 0

for i in ropes:
    sum_ropes += i
    if i > max_rope:
        max_rope = i

sum_ropes_total = sum_ropes - max_rope

if max_rope > sum_ropes_total:
    print(max_rope - sum_ropes_total)
else:
    print(sum_ropes)


