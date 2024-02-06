print(set())
# set()

print(frozenset())
# frozenset()

# Создание непустых изменяемых множеств
s = {'a', 'b', 'c', 'd'}
print(s)
# {'a', 'b', 'c', 'd'}

# При преобразовании последовательности в 
# множество удаляются дубликаты элементов
line = 'abracadabra'
a = set(line)
print(a)
# {'a', 'r', 'd', 'c', 'b'}

lst = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
b = set(lst)
print(b)
# {'a', 'b', 'c', 'd'}

# Добавление элемента к изменяемому множеству
print(a.add(10))
# {'a', 10, 'r', 'd', 'c', 'b'}

# Удаление элемента из изменяемого множества
# происходит по его значению
print(a.remove('r'))
print(a)
# {'a', 10, 'd', 'c', 'b'}

# Метод `.pop()` извлекает и удаляет случайный элемент
# изменяемого множества
print(a.pop())
# 'a'

# НЕИЗМЕНЯЕМОЕ МНОЖЕСТВО
lst = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
s = frozenset(lst)
print(s)
# frozenset({0, 1, 2, 3, 4})
