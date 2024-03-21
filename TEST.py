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


lst = [str(i) + 'q' for i in range(10)]
print(lst)

for i in lst:
    if i == '8q':
        print('FIND')

lst.pop(8)
print(lst)

print(tuple(range(1, 4)))

n = 5
mystr = '5 4 3 2 1'

d = {k: v for k, v in zip(range(n), mystr.split())}
print(d)

print(d[1])
print(d[-1])
