def preview(x):
    print(f'\n---- dict.{x} ----')


def preview2(x):
    print(f'\n---- {x} ----')


x = {'qwe': 1, 'asd': 2, 'zxc': 3}

preview('clear()')
# Очистить словарь. Удалить все элементы из словаря
d = x
print(d)
print(d.clear())

preview('copy()')
# Создать неглубокую копию словаря
d = {'qwe': 1, 'asd': 2, 'zxc': 3}
y = d.copy()

d['qwe'] = 99
del d['asd']
print(d)
print(y)

preview('fromkeys()')
# Создание словаря dict со значениями ключей по умолчанию
d = dict.fromkeys(['Q', 'W', 'E', 'R'])
print(d)
d = dict.fromkeys(['Q', 'W', 'E', 'R'], 'default')
print(d)

print('')
key_list = ['Q', 'W', 'E', 'R']
value_list = [i for i in range(5)]

d = {k: v for k, v in zip(key_list, value_list)}
print(d)

print('')
text = 'quesadilla taco burrito avocado'.split()
y = [i for i in range(len(text))]
d = {k: v for k, v in zip(text, y)}

print(text)
print(y)
print(d)

print('')
key_set = set([i for i in range(11)])
print(key_set)
d = dict.fromkeys(key_set, 0)
print(d)

count = 0
for key in d:
    d[key] = count
    count += 1
print(d)

preview('get()')
# Значение по умолчанию для отсутствующих ключей в словаре
x = {'qwe': 1, 'asd': 2, 'zxc': 3}
d = x
print(d)
print(d.get('qwe', 0))
print(d.get('rty', 0))

print('')
lst = [9, 13, 1, 3, 7, 3, 1, 1, 7, 1, 7, 9]
d = {}

for i in lst:
    if d.get(i, None):
        d[i] += 1
    else:
        d[i] = 1

print(lst)
print(d)
d_sorted = sorted(d.items(), key=lambda i: i[1], reverse=True)
print(dict(d_sorted))

preview('.items()')
# Преобразование словаря в список кортежей ключ-значение
d = x
print(d)

d_items = d.items()
print(d_items)

d['qwe'] = 99
print(d_items)

preview('keys()')
# Получить список-представление всех ключей словаря dict
d = x
print(d)

d_keys = d.keys()
print(d.keys())

d['newone'] = 100
print(d_items)

preview('values()')
# Получение списка всех значений словаря dict
d = x
print(d)
d_values = d.values()
print(d_values)

d['QWERTY'] = 999
print(d_values)

del d['newone']
print(d_values)

preview('pop()')
# Получить значение словаря по ключу и удалить его
print(d)
print(f'dict.pop("QWERTY") = {d.pop("QWERTY")}')
print(d)

preview('popitem()')
# Удалит и вернет двойной кортеж (key, value) из словаря. Пары возвращаются с конца словаря
print(d)
print('')
print(f'dict.popitem() = {d.popitem()}')
print(d)
print('')
print(f'dict.popitem() = {d.popitem()}')
print(d)

preview('setdefault()')
# Получить/добавить значение ключа, если его нет
x = {'qwe': 1, 'asd': 2, 'zxc': 3}
d = x
print(d)
print(f'dict.setdefault("qwe") = {d.setdefault("qwe")}')
print(f'\ndict.setdefault("QWERTY", 0) = {d.setdefault("QWERTY", 0)}')
print(d)

print(f'\ndict.setdefault("QWERTY", 66) = {d.setdefault("QWERTY", 66)}')
print(d)

preview('update()')
# Обновить или дополнить исходный словарь, ключами и значениями другого словаря
print(d)
di = {'quesadilla': 0, 'taco': 1, 'burrito': 2, 'avocado': 3}
print(di)
d.update(di)
print(d)
dic = {'zxc': 999, 'QWERTY': 999, 'quesadilla': 999}
print(f'                    {dic}')
d.update(dic)
print(d)

preview2('reversed()')
# Вывод ключей словаря в обратном порядке
x = {'one': 1, 'two': 2, 'three': 3}
print(x)
print(dict(reversed(x.items())))

preview2('{**dict, **dict} / dict1 | dict2')
# Объединение или слияние двух словарей в один новый словарь
x = {"key1": "value1 from x", "key2": "value2 from x"}
y = {"key2": "value2 from y", "key3": "value3 from y"}
print(x)
print(y, '\n')

print('{**x, **y}\t=', {**x, **y})
print('x | y\t\t=', x | y)

print('{**y, **x}\t=', {**y, **x})
print('y | x\t\t=', y | x)

#
