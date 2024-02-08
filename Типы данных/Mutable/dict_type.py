d = {"one": 1, "two": 2, "three": 3, "four": 4}
print(d)
# {'one': 1, 'two': 2, 'three': 3, 'four': 4}

print(list(d))
# ['one', 'two', 'three', 'four']
print(list(d.values()))
# [1, 2, 3, 4]

d["one"] = 42
print(d)
# {'one': 42, 'two': 2, 'three': 3, 'four': 4}

del d["two"]
d["two"] = None
print(d)
# {'one': 42, 'three': 3, 'four': 4, 'two': None}


d = {"one": 1, "two": 2, "three": 3, "four": 4}
print(d)
# {'one': 1, 'two': 2, 'three': 3, 'four': 4}

print(list(reversed(d)))
# ['four', 'three', 'two', 'one']

print(list(reversed(d.values())))
# [4, 3, 2, 1]

print(list(reversed(d.items())))
# [('four', 4), ('three', 3), ('two', 2), ('one', 1)]

# Создание словаря \ Генерация словаря

lst = [i for i in range(10)]
print(lst)
d = {k: v for k, v in zip(range(10), lst)}
print(d)

d = {i: i * 10 for i in range(10)}
print(d)

d = {(x, y): x + y for x, y in zip('12345', 'QWERTY')}
print(d)

