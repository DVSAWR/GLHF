def preview(x):
    print(f'\n---- sequence.{x} ----')


preview('append()')
# Операция позволяет добавить в конец последовательности новый объект
seq = [1, 2, 3]
print(seq)
seq.append(4)
print(seq)

preview('extend()')
# Добавляет несколько значений в конец списка
seq = [1, 2, 3]
print(seq)
seq.extend([4, 5, 6])
print(seq)

preview('insert()')
# Добавление элемент в список по номеру индекса
seq = [1, 2, 3]
print(seq)
seq.insert(0, 4)
print(seq)

preview('remove()')
# Операция позволяет удалить первый совпавший элемент последовательности
seq = [1, 2, 3, 'qwe']
print(seq)
seq.remove('qwe')
print(seq)

preview('pop()')
# Метод позволяет получить элемент по индексу удаляя его из последовательности.
seq = [1, 2, 3, 'qwe']
print(seq)
seq.pop()
print(seq)
seq.pop(1)
print(seq)

preview('clear')
# Операция удаления всех элементов из последовательности
seq = [1, 2, 3, 'qwe']
print(seq)
seq.clear()
print(seq)

seq = [1, 2, 3, 'qwe']
print(seq)
del seq[:]
print(seq)

preview('index()')
# Индекс первого появления элемента в последовательности
seq = [1, 2, 3, 'qwe']
print(seq)
print(seq.index(1))
print(seq.index('qwe'))

preview('count()')
# Количество вхождений элемента в последовательности
seq = [i // 2 for i in range(9)]
print(seq)
print(f'0 = {seq.count(0)}')
print(f'4 = {seq.count(4)}')

preview('sort()')
# list.sort() сортирует список на месте, используя только оператор сравнения между элементами
li = [5, 2, 3, 1, 4]
print(li)
li.sort()
print(li, '\n')

li = [5, 2, 3, 1, 4]
print(li)
li.sort(reverse=True)
print(li, '\n')

li = ['qqqqq', 'w', 'eee', 'rr']
print(li)
li.sort(key=len)
print(li)

preview('reverse()')
# Реверс элементов списка в Python
seq = [i for i in range(10)]
print(seq)
seq.reverse()
print(seq)

preview('copy()')
# Создание неглубокой копии списка
seq = [i for i in range(10)]
print(seq)
print(f'id {id(seq)}')

seq_2 = seq.copy()
print(seq_2)
print(f'id {id(seq_2)}')

print(f'id == id = {id(seq_2) == id(seq)}')





