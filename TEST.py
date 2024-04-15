y = '''



'''

li = y.split('\n')
print(li)

methods = []
comment_list = []

for i in li:
    if i.startswith('preview'):
        methods.append(i[9:-2])
    if i.startswith('#'):
        comment_list.append(i[2:])

print('\n---- lists ----')
print(methods)
print(comment_list)

di = dict(zip(methods, comment_list))
print(di, '\n')

for i in di:
    print(f'| {i} | {di[i]} |')

lst = [(7, 715477619, 181424399, 534053220), (2, 822889311, 446755913, 376133398), (4, 480845266, 448565595, 32279671),
       (5, 561330066, 605997004, -44666938), (3, 135599877, 389312924, -253713047),
       (1, 160714711, 449656269, -288941558), (6, 61020590, 573085537, -512064947)]
# 1503796355
# 2 4 7 5 1 3 6

print('\n')
print(534053220 + 32279671 + 822889311)
print(376133398 + 32279671 + 534053220 + 561330066)
print('\n')

# smth = 0
#
# for i in range(7):
#     print(lst[i][3])
#     smth += lst[i][3]
#     print(smth + lst[i + 1][1])


sum = 0
numbers = [7, 5, 8, 11, 2, 5, 4, 2, 2, 2]

for i in numbers:
    if i % 2 == 0:
        sum += i

print(sum)


class Person:
    def __init__(self, age):
        self.age = age


p = Person(25)
print(p.age)

p.age = 30
print(p.age)

print('\n')
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end='\t')
        if j == 9:
            print('')

print('\n')
num = 1234
lst = []

print(f'lst = {lst}')
print(f'num = {num}')

while num != 0:
    lst.append(num % 10)
    print(f'lst = {lst}')
    num = num // 10
    print(f'num = {num}')

print('YES' if 2 in lst else 'NO')

print('\n\n---- ALGORITHM EASY TASKS ----')

print('\nTASK 1')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

answer = ""
for i in a:
    if i > 5:
        answer += str(i) + " "
print(answer)

for i in a:
    if i > 5:
        print(i, end=" ")
print('')

print(list(i for i in a if i > 5))
print([i for i in a if i > 5])

print('\nTASK 2')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

answer = []

for i in a:
    if i in b:
        answer.append(i)
print(answer)

print(list(set(a) & set(b)))

print([i for i in a if i in b])

print(list(filter(lambda i: i in b, a)))

print('\nTASK 3')
d = {k: v for k, v in zip('tacos', range(5))}

print(sorted(d.items(), key=lambda item: item[1]))
print(sorted(d.items(), key=lambda item: item[1], reverse=True))

print('\nTASK 4')
d = {k: v for k, v in zip('tacos', range(10))}
d2 = {k: v for k, v in zip('burrito', range(10))}
print(d)
print(d2)

answer = {}

for i in (d, d2):
    answer.update(i)
print(answer)

answer = {**d, **d2}
print(answer)

answer = dict(list(d.items()) + list(d2.items()))
print(answer)

print('')
from itertools import chain

all = {}
for k, v in chain(d.items(), d2.items()):
    if k in all:
        if all[k] < v:
            all[k] = 'QWE'
    else:
        all[k] = v

print(all)

print('\nTASK 5')
d3 = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
print(d3)

my_dict = dict(sorted(d3.items(), key=lambda item: item[1], reverse=True))
print(my_dict)

answer = list(my_dict.values())[:3]
print(*answer)

answer = list(sorted(d3.values(), reverse=True))[:3]
print(*answer)

for i in list(sorted(d3.values(), reverse=True))[:3]:
    print(i, end=" ")
print('')

print('\nTASK 6')

print(int('ABC', 16))
print(int('-0xf', base=16))
print(int('0b111', base=2))

print('\nTASK 7')


def pascal_triangle(n):
    row = [1]
    for i in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row, row)]


pascal_triangle(6)

n = 6
