'''

Домашний питомец мальчика Васи — улитка Петя. Петя обитает на бесконечном в обе стороны вертикальном столбе, который для удобства можно представить как числовую прямую. Изначально Петя находится в точке
0
.
Вася кормит Петю ягодами. У него есть
n
 ягод, каждая в единственном экземпляре. Вася знает, что если утром он даст Пете ягоду с номером
i
, то поев и набравшись сил, за остаток дня Петя поднимется на
a
i
 единиц вверх по столбу, но при этом за ночь, потяжелев, съедет на
b
i
 единиц вниз. Параметры различных ягод могут совпадать.
Пете стало интересно, а как оно там, наверху, и Вася взялся ему в этом помочь. Ближайшие
n
 дней он будет кормить Петю ягодами из своего запаса таким образом, чтобы максимальная высота, на которой побывал Петя за эти
n
 дней была максимальной. К сожалению, Вася не умеет программировать, поэтому он попросил вас о помощи. Найдите, максимальную высоту, на которой Петя сможет побывать за эти
n
 дней и в каком порядке Вася должен давать Пете ягоды, чтобы Петя смог её достичь!

Формат ввода
В первой строке входных данных дано число
n
 (
1
≤
n
≤
5
⋅
1
0
5
) — количество ягод у Васи. В последующих
n
 строках описываются параметры каждой ягоды. В
i
+
1
 строке дано два числа
a
i
 и
b
i
 (
0
≤
a
i
,
b
i
≤
1
0
9
) — то, насколько поднимется улитка за день после того, как съест
i
 ягоду и насколько опуститься за ночь.
Формат вывода
В первой строке выходных данных выведите единственное число — максимальную высоту, которую сможет достичь Петя, если Вася будет его кормить оптимальным образом. В следующей строке выведите
n
 различных целых чисел от
1
 до
n
 — порядок, в котором Вася должен кормить Петю (
i
 число в строке соответствует номеру ягоды, которую Вася должен дать Пете в
i
 день чтобы Петя смог достичь максимальной высоты).
Пример 1
Ввод
3
1 5
8 2
4 4
10

Вывод
2 3 1

Пример 2
Ввод
2
7 6
7 4
10

Вывод
2 1

'''

#
# print('\n-------------TRY-------------\n')

# # INPUT
#
# n = int(input())
# berry = []
#
# for i in range(n):
#     position = i + 1
#     b, d = map(int, input().split())
#     value = b - d
#     berry.append((position, b, d, value))
#
# print(berry)
#
# sorted_berry_value = sorted(berry, key=lambda item: item[3], reverse=True)
#
# print('\nSORT BY VALUE:', sorted_berry_value)
#
# # n = 6
# #
# # berry = [(1, 1, 1, 0), (2, 4, 4, 0), (3, 100, 200, -100), (4, 0, 50, -50), (5, 50, 1, 49), (6, 1, 50, -49)]
# #
#
# # n = 6
# # sorted_berry_value = [(5, 50, 1, 49), (1, 1, 1, 0), (2, 4, 4, 0), (6, 1, 50, -49), (4, 0, 50, -50), (3, 100, 200, -100)]
#
#
# max_buff_berry = 0
# max_buff_berry_index = None
#
# for i in range(n):
#     if sorted_berry_value[i][1] > max_buff_berry:
#         max_buff_berry = sorted_berry_value[i][1]
#         max_buff_berry_index = i
#         print(max_buff_berry)
#
# max_buff_berry = sorted_berry_value[max_buff_berry_index]
#
# print('\nMAX BERRY:', max_buff_berry, '\nMAX BERRY INDEX:', max_buff_berry_index)
#
# # 0 - b index
# # 1 - b buff
# # 2 - b debuff
# # 3 - b value
#
# maximum_position = 0
# current_position = 0
#
# find_max_buff_berry = 0
#
# berry_sequence = []
#
# for i in range(n):
#
#     if sorted_berry_value[i][3] > 0:
#
#         current_position += sorted_berry_value[i][1]
#         if current_position > maximum_position:
#             maximum_position = current_position
#         current_position -= sorted_berry_value[i][2]
#
#         if i == max_buff_berry:
#             find_max_buff_berry = 1
#
#         berry_sequence.append(sorted_berry_value[i][0])
#
#     else:
#         if find_max_buff_berry:
#             berry_sequence.append(sorted_berry_value[i][0])
#         else:
#             berry_sequence.append(sorted_berry_value[max_buff_berry_index][0])
#
#             maximum_position = current_position + sorted_berry_value[max_buff_berry_index][1]
#
#             if n > 2:
#                 tail = sorted_berry_value[i:max_buff_berry_index] + sorted_berry_value[max_buff_berry_index + 1:]
#                 print('\nTAIL:', tail)
#                 for i in range(len(tail)):
#                     berry_sequence.append(tail[i][0])
#
#             break
#
# print(f'\n\nMAX POS: {maximum_position}\nBERRY SEQ: {berry_sequence}')
#
# print('\n')
#
#
# print('\n--------------DONE---------\n')
#
# print(maximum_position)
# print(' '.join(map(str, berry_sequence)))


# 822889311 446755913 480845266 448565595 715477619 181424399
#
# 534053220 32279671 822889311

# 7
# 160714711 449656269
# 822889311 446755913
# 135599877 389312924
# 480845266 448565595
# 561330066 605997004
# 61020590 573085537
# 715477619 181424399

# 1503796355
# 2 4 7 5 1 3 6


print('\n--------xxxxxxxxx-------\n')

# n = 7
# berry = [(7, 715477619, 181424399, 534053220), (2, 822889311, 446755913, 376133398),
#          (4, 480845266, 448565595, 32279671), (5, 561330066, 605997004000, -605435673934),
#          (3, 135599877, 389312924, -253713047), (1, 160714711, 449656269, -288941558),
#          (6, 61020590, 573085537, -512064947)]
# 1503796355
# 2 4 7 5 1 3 6


n = int(input())

left = []
right = []

nleft = 0
nright = 0


for i in range(n):
    position = i + 1
    b, d = map(int, input().split())
    value = b - d
    if value > 0:
        left.append((position, b, d, value))
        nleft += 1

    else:
        right.append((position, b, d, value))
        nright += 1

# n = 7
# left = [(2, 822889311, 446755913, 376133398), (4, 480845266, 448565595, 32279671), (7, 715477619, 181424399, 534053220)]
# right = [(1, 160714711, 449656269, -288941558), (3, 135599877, 389312924, -253713047), (5, 561330066, 605997004, -44666938), (6, 61020590, 573085537, -512064947)]


print('LEFT:\n', left)
print(f'LEN: {nleft}')
print('RIGHT:\n', right)
print(f'LEN: {nright}')

sorted_left = sorted(left, key=lambda item: item[3], reverse=True)
sorted_right = sorted(right, key=lambda item: item[1], reverse=True)

print(f'\nSORTED LEFT:\n{sorted_left}\n\nSORTED RIGHT:\n{sorted_right}')

maximum_position = 0
current_position = 0
berry_seq = []

for i in range(nleft):
    current_position += sorted_left[i][1]
    if current_position > maximum_position:
        maximum_position = current_position
    current_position -= sorted_left[i][2]
    berry_seq.append(sorted_left[i][0])

if nright != 0:
    if maximum_position < current_position + sorted_right[0][1]:
        maximum_position = current_position + sorted_right[0][1]

    for i in sorted_right:
        berry_seq.append(i[0])

print(f'\nMAX POS: {maximum_position}\nCUR POS: {current_position}')
print(berry_seq)

print('\n-------TEST--------\n')


n = int(input())

left = []
right = []

nleft = 0
nright = 0

for i in range(n):
    position = i + 1
    b, d = map(int, input().split())
    value = b - d
    if value > 0:
        left.append((position, b, d, value))
        nleft += 1

    else:
        right.append((position, b, d, value))
        nright += 1

sorted_left = sorted(left, key=lambda item: item[3], reverse=True)
sorted_right = sorted(right, key=lambda item: item[1], reverse=True)

maximum_position = 0
current_position = 0
berry_seq = []

for i in range(nleft):
    current_position += sorted_left[i][1]
    if current_position > maximum_position:
        maximum_position = current_position
    current_position -= sorted_left[i][2]
    berry_seq.append(sorted_left[i][0])

if nright != 0:
    if maximum_position < current_position + sorted_right[0][1]:
        maximum_position = current_position + sorted_right[0][1]

    for i in sorted_right:
        berry_seq.append(i[0])

print(maximum_position)
print(' '.join(map(str, berry_seq)))



# TEST

