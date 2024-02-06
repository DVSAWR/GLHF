# Примеры операций со словарями:
d = {"one": 1, "two": 2, "three": 3, "four": 4}
print(d)
# {'one': 1, 'two': 2, 'three': 3, 'four': 4}

# гарантированное сохранение порядка вставки
print(list(d))
# ['one', 'two', 'three', 'four']
print(list(d.values()))
# [1, 2, 3, 4]

# обновление ключа не влияет на порядок
d["one"] = 42
print(d)
# {'one': 42, 'two': 2, 'three': 3, 'four': 4}

# После удаления, ключ вставляются в конец словаря
del d["two"]
d["two"] = None
print(d)
# {'one': 42, 'three': 3, 'four': 4, 'two': None}


# Словари и словарные представления стали обратимы:

d = {"one": 1, "two": 2, "three": 3, "four": 4}
print(d)
# {'one': 1, 'two': 2, 'three': 3, 'four': 4}

print(list(reversed(d)))
# ['four', 'three', 'two', 'one']

print(list(reversed(d.values())))
# [4, 3, 2, 1]

print(list(reversed(d.items())))
# [('four', 4), ('three', 3), ('two', 2), ('one', 1)]
