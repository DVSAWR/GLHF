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
