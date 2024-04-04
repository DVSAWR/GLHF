print(set())
# set()

print(frozenset())
# frozenset()

s = {'a', 'b', 'c', 'd'}
print(s)
# {'a', 'b', 'c', 'd'}

line = 'abracadabra'
a = set(line)
print(a)
# {'a', 'r', 'd', 'c', 'b'}

lst = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
b = set(lst)
print(b)
# {'a', 'b', 'c', 'd'}

print(a.add(10))
# {'a', 10, 'r', 'd', 'c', 'b'}

print(a.remove('r'))
print(a)
# {'a', 10, 'd', 'c', 'b'}

print(a.pop())
# 'a'

# FROZENSET
lst = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
s = frozenset(lst)
print(s)
# frozenset({0, 1, 2, 3, 4})
