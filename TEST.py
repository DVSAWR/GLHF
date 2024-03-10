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
